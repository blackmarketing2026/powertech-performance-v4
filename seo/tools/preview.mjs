// Read-only local preview using Vercel's compiled route patterns.
// Run after compiling vercel.json with @vercel/routing-utils (see validation report).
import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../..');
const compiled=JSON.parse(fs.readFileSync(path.join(root,'seo/routing-compiled.json'),'utf8'));
if(compiled.error)throw new Error(JSON.stringify(compiled.error));
const routes=compiled.routes.filter(r=>r.src).map(r=>({...r,re:new RegExp(r.src)}));
const mime={'.html':'text/html; charset=utf-8','.css':'text/css; charset=utf-8','.js':'text/javascript; charset=utf-8','.png':'image/png','.jpg':'image/jpeg','.jpeg':'image/jpeg','.webp':'image/webp','.svg':'image/svg+xml','.woff2':'font/woff2','.xml':'application/xml','.txt':'text/plain'};
const server=http.createServer((req,res)=>{
  if(!['GET','HEAD'].includes(req.method)){res.writeHead(405);res.end('Read-only preview');return;}
  const u=new URL(req.url,'http://127.0.0.1:4173');
  let pathname;try{pathname=decodeURIComponent(u.pathname);}catch{res.writeHead(400);res.end();return;}
  if(/^\/(seo|api|Datei Manager|node_modules|\.git)(\/|$)/i.test(pathname)){res.writeHead(404);res.end();return;}
  for(const r of routes){
    if(r.status>=300&&r.status<400&&r.re.test(pathname)){
      res.writeHead(r.status,{Location:r.headers.Location+u.search});res.end();return;
    }
  }
  const rewrite=routes.find(r=>r.dest&&r.re.test(pathname));
  let relative=rewrite?.dest||pathname;
  if(relative.endsWith('/'))relative+='index.html';
  const filename=path.resolve(root,'.'+relative);
  if(!filename.startsWith(root+path.sep)||!fs.existsSync(filename)||!fs.statSync(filename).isFile()){
    res.writeHead(404);res.end('Not found');return;
  }
  if(!['.html','.css','.js','.png','.jpg','.jpeg','.webp','.svg','.woff2','.xml','.txt'].includes(path.extname(filename))){res.writeHead(404);res.end();return;}
  res.writeHead(200,{'Content-Type':mime[path.extname(filename)],'Cache-Control':'no-store','Content-Security-Policy':"default-src 'self' data:; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; font-src 'self'; connect-src 'self'; frame-src 'none'; form-action 'none'"});
  res.end(req.method==='HEAD'?undefined:fs.readFileSync(filename));
});
server.listen(Number(process.env.PORT || 4173),'127.0.0.1',()=>console.log('Read-only preview http://127.0.0.1:4173; external tracking blocked by preview CSP'));

"""Targeted QA follow-ups; idempotent changes, no runtime/form changes."""
from pathlib import Path
import json,re
R=Path(__file__).resolve().parents[2]
p=R/'glosar.html';s=p.read_text('utf8')
old='Professionelle Fahrzeugaufbereitung innen und außen. In Erfurt sorgt Powertech Performance für glänzende Ergebnisse und Werterhalt.'
new='Professionelle Fahrzeugaufbereitung umfasst gezielte Pflege innen und außen. Wie sich der Bedarf einschätzen lässt, erklärt der Ratgeber <a href="/blog/wie-oft-auto-aufbereiten-lassen.html">Wie oft das Auto aufbereiten lassen?</a>'
s=s.replace(old,new);p.write_text(s,encoding='utf8')
p=R/'trockeneisreinigung.html';s=p.read_text('utf8')
s=s.replace('Daraus folgt keine Aussage darüber, welches Gerät an Ihrem Fahrzeug verwendet wird oder welches Ergebnis möglich ist.','Die Eignung der Methode wird für die betroffenen Fahrzeugbereiche individuell besprochen.')
s=s.replace('Ohne Kenntnis des Fahrzeugs und des gewünschten Umfangs nennen wir hier keinen Pauschalpreis und keine feste Dauer.','Der Aufwand richtet sich nach dem Fahrzeug, der Zugänglichkeit und dem gewünschten Reinigungsumfang. Eine Einschätzung zu Kosten und Zeit erhalten Sie im persönlichen Gespräch.')
p.write_text(s,encoding='utf8')
# Keep original compact formatting in routing config for review.
p=R/'vercel.json';c=json.loads(p.read_text('utf8'))
out=['{','  "redirects": [']
out+=['    '+json.dumps(v,ensure_ascii=False)+(',' if i<len(c['redirects'])-1 else '') for i,v in enumerate(c['redirects'])]
out+=['  ],','  "rewrites": [']
out+=['    '+json.dumps(v,ensure_ascii=False)+(',' if i<len(c['rewrites'])-1 else '') for i,v in enumerate(c['rewrites'])]
out+=['  ]','}'];p.write_text('\n'.join(out)+'\n',encoding='utf8')

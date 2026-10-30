const Footer = () => {
  return (
    <footer className="bg-card border-t border-border py-8 md:py-12">
      <div className="container px-4">
        <div className="max-w-6xl mx-auto">
          <div className="grid md:grid-cols-3 gap-8 mb-6">
            <div>
              <h3 className="text-xl font-bold mb-4 text-primary">PowerTech Performance</h3>
              <p className="text-muted-foreground">
                Professionelle Keramikversiegelung und Fahrzeugpflege in Erfurt.
              </p>
            </div>

            <div>
              <h4 className="font-semibold mb-4">Kontakt</h4>
              <address className="text-muted-foreground not-italic">
                An der Klinge 10<br />
                99095 Erfurt<br />
                <a href="tel:+491737373574" className="hover:text-primary transition-colors">
                  +49 173 7373574
                </a><br />
                <a href="mailto:info@powertech-performance.de" className="hover:text-primary transition-colors">
                  info@powertech-performance.de
                </a>
              </address>
            </div>

            <div>
              <h4 className="font-semibold mb-4">Service</h4>
              <ul className="space-y-2 text-muted-foreground">
                <li>Keramikversiegelung</li>
                <li>Lackaufbereitung</li>
                <li>Fahrzeugpflege</li>
                <li>Detailing</li>
              </ul>
            </div>
          </div>

          <div className="border-t border-border pt-8 text-center">
            <div className="flex flex-wrap justify-center gap-6 mb-4 text-sm">
              <a
                href="/pages/impressum.html"
                target="_blank"
                rel="noopener noreferrer"
                className="text-muted-foreground hover:text-primary transition-colors"
              >
                Impressum
              </a>
              <a
                href="/pages/datenschutz.html"
                target="_blank"
                rel="noopener noreferrer"
                className="text-muted-foreground hover:text-primary transition-colors"
              >
                Datenschutz
              </a>
            </div>
            <p className="text-muted-foreground">
              © {new Date().getFullYear()} PowerTech Performance – Inhaber: Benjamin Lemmer. Alle Rechte vorbehalten.
            </p>
          </div>
        </div>
      </div>
    </footer>
  );
};

export default Footer;

import { Award, CheckCircle2, Wrench } from "lucide-react";
import benjaminImage from "@/assets/benjamin-lemmer.png";

const About = () => {
  return (
    <section className="py-16 md:py-24 bg-background">
      <div className="container px-4">
        <div className="max-w-6xl mx-auto">
          <div className="text-center mb-12">
            <h2 className="text-3xl md:text-5xl font-bold mb-4">
              Persönliche Fahrzeugpflege
            </h2>
            <p className="text-xl text-muted-foreground">
              Ihr Fahrzeug in den besten Händen
            </p>
          </div>

          <div className="grid md:grid-cols-2 gap-12 items-center">
            {/* Image */}
            <div className="order-2 md:order-1">
              <div className="relative rounded-2xl overflow-hidden shadow-xl">
                <img
                  src={benjaminImage}
                  alt="Benjamin Lemmer bei der professionellen Fahrzeugaufbereitung"
                  className="w-full h-auto"
                />
                <div className="absolute bottom-0 left-0 right-0 bg-gradient-to-t from-background/95 via-background/70 to-transparent p-6">
                  <div className="flex items-center gap-3">
                    <div className="w-12 h-12 bg-primary rounded-full flex items-center justify-center">
                      <Award className="w-6 h-6 text-primary-foreground" />
                    </div>
                    <div>
                      <p className="font-bold text-lg">Benjamin Lemmer</p>
                      <p className="text-sm text-muted-foreground">Inhaber und Fahrzeugaufbereiter</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            {/* Content */}
            <div className="order-1 md:order-2 space-y-6">
              <div>
                <h3 className="text-2xl md:text-3xl font-bold mb-4">
                  Benjamin Lemmer – Ihr Experte für Perfektion
                </h3>
                <p className="text-lg text-muted-foreground leading-relaxed">
                  Benjamin Lemmer ist Inhaber und Fahrzeugaufbereiter bei Powertech Performance. Er bespricht mit Ihnen den Zustand des Fahrzeugs und welche Pflege zu Ihren Wünschen passt.
                </p>
              </div>

              <div className="bg-card border border-border rounded-xl p-6 space-y-4">
                <div className="flex items-start gap-3">
                  <CheckCircle2 className="w-6 h-6 text-primary flex-shrink-0 mt-1" />
                  <div>
                    <p className="font-semibold mb-1">Persönliche Beratung</p>
                    <p className="text-muted-foreground text-sm">
                      Leistungen und Umfang werden am Fahrzeug abgestimmt
                    </p>
                  </div>
                </div>

                <div className="flex items-start gap-3">
                  <Wrench className="w-6 h-6 text-primary flex-shrink-0 mt-1" />
                  <div>
                    <p className="font-semibold mb-1">Sorgfältige Vorbereitung</p>
                    <p className="text-muted-foreground text-sm">
                      Reinigung und Lackvorbereitung passend zum Zustand
                    </p>
                  </div>
                </div>

                <div className="flex items-start gap-3">
                  <Award className="w-6 h-6 text-primary flex-shrink-0 mt-1" />
                  <div>
                    <p className="font-semibold mb-1">Höchste Qualitätsstandards</p>
                    <p className="text-muted-foreground text-sm">
                      Vom ersten Handgriff bis zum letzten Detail – professionell und präzise
                    </p>
                  </div>
                </div>
              </div>

              <p className="text-lg text-muted-foreground leading-relaxed">
                Vom ersten Handgriff bis zum letzten Blick fürs Detail steht eines im Mittelpunkt:{" "}
                <strong className="text-foreground">Ihr Fahrzeug soll aussehen, als wäre es gerade neu geboren.</strong>{" "}
                Egal ob Alltag, Verkauf oder Werterhalt: Benjamin Lemmer versteht, was echte Aufbereitung bedeutet – und was sie leisten muss.
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default About;

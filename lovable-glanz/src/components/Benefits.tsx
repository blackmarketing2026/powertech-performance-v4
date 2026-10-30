import { Shield, Droplets, Sparkles, Clock, TrendingUp } from "lucide-react";

const Benefits = () => {
  const benefits = [
    {
      icon: Shield,
      title: "Schutz vor UV-Strahlung, Streusalz und Insekten",
      description: "Die keramische Schutzschicht bildet eine dauerhafte Barriere gegen Umwelteinflüsse.",
    },
    {
      icon: Droplets,
      title: "Extrem hydrophobe Oberfläche",
      description: "Wasser perlt ab wie bei einem Lotusblatt – Schmutz hat keine Chance.",
    },
    {
      icon: Sparkles,
      title: "Leichter zu reinigen",
      description: "Weniger Waschaufwand durch selbstreinigende Eigenschaften der Versiegelung.",
    },
    {
      icon: TrendingUp,
      title: "Erhöhter Wiederverkaufswert",
      description: "Perfekt erhaltener Lack steigert den Wert Ihres Fahrzeugs messbar.",
    },
    {
      icon: Clock,
      title: "Langanhaltender Schutz",
      description: "Die Haltbarkeit hängt von Nutzung, Pflege und Produkt ab.",
    },
  ];

  return (
    <section className="py-16 md:py-24 bg-gradient-subtle">
      <div className="container px-4">
        <div className="text-center mb-12">
          <h2 className="text-3xl md:text-5xl font-bold mb-4">
            Warum Keramikversiegelung?
          </h2>
          <p className="text-xl text-muted-foreground max-w-2xl mx-auto">
            Investieren Sie in dauerhaften Schutz und perfekten Glanz für Ihr Fahrzeug
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 max-w-6xl mx-auto">
          {benefits.map((benefit, index) => {
            const Icon = benefit.icon;
            return (
              <div
                key={index}
                className="bg-card p-8 rounded-xl shadow-md hover:shadow-xl transition-all border border-border/50"
              >
                <div className="w-14 h-14 bg-gradient-primary rounded-lg flex items-center justify-center mb-6 shadow-glow">
                  <Icon className="w-7 h-7 text-primary-foreground" />
                </div>
                <h3 className="text-xl font-semibold mb-3">{benefit.title}</h3>
                <p className="text-muted-foreground leading-relaxed">
                  {benefit.description}
                </p>
              </div>
            );
          })}
        </div>
      </div>
    </section>
  );
};

export default Benefits;

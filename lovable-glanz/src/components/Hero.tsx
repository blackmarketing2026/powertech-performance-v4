import { Button } from "@/components/ui/button";
import { Shield, Droplets, Sparkles, TrendingUp } from "lucide-react";
import heroImage from "@/assets/hero-car.jpg";

const Hero = () => {
  const scrollToContact = () => {
    document.getElementById("contact")?.scrollIntoView({ behavior: "smooth" });
  };

  return (
    <section className="relative min-h-[90vh] flex items-center justify-center overflow-hidden pt-20">
      {/* Background Image with Overlay */}
      <div className="absolute inset-0 z-0">
        <img
          src={heroImage}
          alt="Hochglänzender Lack mit Keramikversiegelung"
          className="w-full h-full object-cover"
        />
        <div className="absolute inset-0 bg-gradient-to-r from-background/95 via-background/85 to-background/70" />
      </div>

      {/* Content */}
      <div className="container relative z-10 px-4 py-16 md:py-24">
        <div className="max-w-3xl">
          <h1 className="text-4xl md:text-6xl lg:text-7xl font-bold mb-6 leading-tight">
            Keramikversiegelung mit Glanz{" "}
            <span className="text-primary">und Lackschutz</span>
          </h1>

          <p className="text-xl md:text-2xl mb-8 text-muted-foreground">
            Schütze deinen Lack dauerhaft – Glanz, Schutz und Werterhalt in einem.
          </p>

          <Button
            size="lg"
            onClick={scrollToContact}
            className="mb-12 text-lg px-8 py-6 shadow-glow hover:shadow-xl transition-all"
          >
            Jetzt kostenlos anfragen
          </Button>

          {/* Benefits Grid */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div className="flex items-start gap-3 bg-card/80 backdrop-blur-sm p-4 rounded-lg border border-border/50">
              <Shield className="w-6 h-6 text-primary flex-shrink-0 mt-1" />
              <div>
                <p className="font-semibold text-lg">Individuelle Beratung</p>
              </div>
            </div>

            <div className="flex items-start gap-3 bg-card/80 backdrop-blur-sm p-4 rounded-lg border border-border/50">
              <Sparkles className="w-6 h-6 text-primary flex-shrink-0 mt-1" />
              <div>
                <p className="font-semibold text-lg">Professionell aufgetragen in Erfurt</p>
              </div>
            </div>

            <div className="flex items-start gap-3 bg-card/80 backdrop-blur-sm p-4 rounded-lg border border-border/50">
              <Droplets className="w-6 h-6 text-primary flex-shrink-0 mt-1" />
              <div>
                <p className="font-semibold text-lg">Spürbar glatter Lack</p>
              </div>
            </div>

            <div className="flex items-start gap-3 bg-card/80 backdrop-blur-sm p-4 rounded-lg border border-border/50">
              <TrendingUp className="w-6 h-6 text-primary flex-shrink-0 mt-1" />
              <div>
                <p className="font-semibold text-lg">Perfekter Glanz auch nach Jahren</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Hero;

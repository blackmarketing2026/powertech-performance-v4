import { Button } from "@/components/ui/button";
import { ArrowRight } from "lucide-react";

const CTA = () => {
  const scrollToContact = () => {
    document.getElementById("contact")?.scrollIntoView({ behavior: "smooth" });
  };

  return (
    <section className="py-16 md:py-24 bg-gradient-hero relative overflow-hidden">
      <div className="absolute inset-0 bg-[url('data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAiIGhlaWdodD0iNjAiIHZpZXdCb3g9IjAgMCA2MCA2MCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48ZyBmaWxsPSJub25lIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiPjxwYXRoIGQ9Ik0zNiAxOGMzLjMxNCAwIDYgMi42ODYgNiA2cy0yLjY4NiA2LTYgNi02LTIuNjg2LTYtNiAyLjY4Ni02IDYtNnoiIHN0cm9rZT0iI2ZmZiIgc3Ryb2tlLW9wYWNpdHk9Ii4wNSIgc3Ryb2tlLXdpZHRoPSIyIi8+PC9nPjwvc3ZnPg==')] opacity-10" />

      <div className="container px-4 relative z-10">
        <div className="max-w-4xl mx-auto text-center">
          <h2 className="text-3xl md:text-5xl font-bold mb-6 text-primary-foreground">
            Lackschutz für dein Fahrzeug – sichere dir dein Angebot!
          </h2>

          <p className="text-xl md:text-2xl mb-8 text-primary-foreground/90">
            Investiere in dauerhaften Schutz und perfekten Glanz für dein Fahrzeug
          </p>

          <Button
            size="lg"
            onClick={scrollToContact}
            className="bg-primary-foreground text-primary hover:bg-primary-foreground/90 text-lg px-8 py-6 shadow-xl group"
          >
            Kostenlos anfragen
            <ArrowRight className="ml-2 w-5 h-5 group-hover:translate-x-1 transition-transform" />
          </Button>

          <p className="mt-6 text-primary-foreground/80 text-lg">
            Keramikversiegelung in Erfurt – jetzt Termin anfragen!
          </p>
        </div>
      </div>
    </section>
  );
};

export default CTA;

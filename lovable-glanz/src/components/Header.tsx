import { Button } from "@/components/ui/button";
import logo from "@/assets/logo.png";

const Header = () => {
  const scrollToContact = () => {
    document.getElementById("contact")?.scrollIntoView({ behavior: "smooth" });
  };

  return (
    <header className="fixed top-0 left-0 right-0 z-50 bg-background/80 backdrop-blur-md border-b border-border">
      <div className="container px-4 py-4 flex items-center justify-between">
        <div className="flex items-center gap-3">
          <img
            src={logo}
            alt="PowerTech Performance Logo"
            className="h-12 md:h-16 w-auto"
          />
          <div className="text-xl md:text-2xl font-bold text-primary hidden sm:block">
            PowerTech Performance
          </div>
        </div>

        <Button onClick={scrollToContact} size="lg">
          Kostenlos anfragen
        </Button>
      </div>
    </header>
  );
};

export default Header;

import Header from "@/components/Header";
import Hero from "@/components/Hero";
import Benefits from "@/components/Benefits";
import About from "@/components/About";
import Gallery from "@/components/Gallery";
import Guarantee from "@/components/Guarantee";
import FAQ from "@/components/FAQ";
import CTA from "@/components/CTA";
import Contact from "@/components/Contact";
import Footer from "@/components/Footer";

const Index = () => {
  return (
    <div className="min-h-screen">
      <Header />
      <main>
        <Hero />
        <Benefits />
        <About />
        <Gallery />
        <Guarantee />
        <FAQ />
        <CTA />
        <Contact />
      </main>
      <Footer />
    </div>
  );
};

export default Index;

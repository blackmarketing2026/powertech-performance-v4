import { useState } from "react";
import { X } from "lucide-react";
import car1 from "@/assets/gallery/car-1.jpeg";
import car2 from "@/assets/gallery/car-2.jpeg";
import car3 from "@/assets/gallery/car-3.jpeg";
import car4 from "@/assets/gallery/car-4.jpeg";
import car5 from "@/assets/gallery/car-5.jpeg";
import car6 from "@/assets/gallery/car-6.jpeg";
import car7 from "@/assets/gallery/car-7.jpeg";
import car8 from "@/assets/gallery/car-8.jpeg";
import car9 from "@/assets/gallery/car-9.jpeg";
import car10 from "@/assets/gallery/car-10.jpeg";

const Gallery = () => {
  const [selectedImage, setSelectedImage] = useState<string | null>(null);

  const images = [
    { src: car1, alt: "McLaren mit Keramikversiegelung" },
    { src: car2, alt: "SUV mit glänzender Keramikversiegelung" },
    { src: car3, alt: "Wohnmobil mit professioneller Versiegelung" },
    { src: car4, alt: "BMW mit Spiegelglanz-Versiegelung" },
    { src: car5, alt: "Mercedes mit Keramikschutz" },
    { src: car6, alt: "SUV nach Keramikversiegelung" },
    { src: car7, alt: "Fahrzeug mit hydrophober Versiegelung" },
    { src: car8, alt: "Auto mit perfekter Keramikversiegelung" },
    { src: car9, alt: "Versiegeltes Fahrzeug im Außenbereich" },
    { src: car10, alt: "Jaguar mit Premium-Versiegelung" },
  ];

  return (
    <>
      <section className="py-16 md:py-24 bg-muted/30">
        <div className="container px-4">
          <div className="text-center mb-12">
            <h2 className="text-3xl md:text-5xl font-bold mb-4">
              Unsere Referenzen
            </h2>
            <p className="text-xl text-muted-foreground max-w-2xl mx-auto">
              Überzeugen Sie sich von der Qualität unserer Arbeit – echte Kundenfahrzeuge mit professioneller Keramikversiegelung
            </p>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6 max-w-7xl mx-auto">
            {images.map((image, index) => (
              <div
                key={index}
                className="group relative aspect-square overflow-hidden rounded-xl cursor-pointer shadow-md hover:shadow-xl transition-all"
                onClick={() => setSelectedImage(image.src)}
              >
                <img
                  src={image.src}
                  alt={image.alt}
                  className="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110"
                />
                <div className="absolute inset-0 bg-gradient-to-t from-background/80 via-background/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-end p-4">
                  <p className="text-sm font-medium text-primary-foreground">
                    {image.alt}
                  </p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Lightbox Modal */}
      {selectedImage && (
        <div
          className="fixed inset-0 z-50 bg-background/95 backdrop-blur-sm flex items-center justify-center p-4"
          onClick={() => setSelectedImage(null)}
        >
          <button
            className="absolute top-4 right-4 w-10 h-10 bg-card rounded-full flex items-center justify-center hover:bg-primary hover:text-primary-foreground transition-colors shadow-lg"
            onClick={() => setSelectedImage(null)}
          >
            <X className="w-6 h-6" />
          </button>
          <img
            src={selectedImage}
            alt="Vergrößerte Ansicht"
            className="max-w-full max-h-[90vh] object-contain rounded-lg shadow-2xl"
            onClick={(e) => e.stopPropagation()}
          />
        </div>
      )}
    </>
  );
};

export default Gallery;

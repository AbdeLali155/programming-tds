import React from 'react';
import { Download } from 'lucide-react';

const ProbabilityExercises = () => {
  const downloadPDF = () => {
    const content = document.getElementById('pdf-content');
    const opt = {
      margin: 15,
      filename: 'Exercices_5_6_Probabilite.pdf',
      image: { type: 'jpeg', quality: 0.98 },
      html2canvas: { scale: 2 },
      jsPDF: { unit: 'mm', format: 'a4', orientation: 'portrait' }
    };
    
    // Using html2pdf library
    if (window.html2pdf) {
      window.html2pdf().set(opt).from(content).save();
    } else {
      alert('Chargement de la bibliothèque PDF...');
      const script = document.createElement('script');
      script.src = 'https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js';
      script.onload = () => {
        window.html2pdf().set(opt).from(content).save();
      };
      document.head.appendChild(script);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 p-8">
      <div className="max-w-4xl mx-auto">
        <div className="bg-white rounded-lg shadow-xl p-8 mb-6">
          <div className="flex justify-between items-center mb-6">
            <h1 className="text-3xl font-bold text-indigo-900">
              Solutions Complètes - Exercices 5 & 6
            </h1>
            <button
              onClick={downloadPDF}
              className="flex items-center gap-2 bg-indigo-600 hover:bg-indigo-700 text-white px-6 py-3 rounded-lg font-semibold transition-colors shadow-md"
            >
              <Download size={20} />
              Télécharger PDF
            </button>
          </div>
          
          <div className="bg-blue-50 border-l-4 border-blue-500 p-4 mb-6">
            <p className="text-blue-900 font-semibold">
              📚 Module: Probabilité | TD 2 | Année 2024/2025
            </p>
            <p className="text-blue-800 text-sm mt-1">
              École Normale Supérieure de l'Enseignement Technique de Mohammedia
            </p>
          </div>
        </div>

        <div id="pdf-content" className="bg-white rounded-lg shadow-xl p-10">
          
          {/* Exercice 5 */}
          <div className="mb-12">
            <h2 className="text-2xl font-bold text-indigo-900 mb-6 pb-2 border-b-2 border-indigo-200">
              Exercice 5
            </h2>
            
            <div className="bg-gray-50 p-6 rounded-lg mb-6">
              <h3 className="font-bold text-lg mb-3">📋 Énoncé:</h3>
              <p className="mb-3">Soit (Ω, B, P) un espace probabilisé. X est une v.a.d définie sur B dont la loi de probabilité est définie par:</p>
              <div className="bg-white p-4 rounded border-2 border-gray-200 text-center my-4">
                <p>P(X = 1) = p,   P(X₁ = -1) = q,   P(X = 0) = 1 - p - q</p>
              </div>
              <p>Soit Y une v.a.d définie sur B, de même loi que X, telles que X et Y soient indépendantes.</p>
              <p className="mt-2">On pose Z = X + Y</p>
            </div>

            {/* Question 1 */}
            <div className="mb-8">
              <h3 className="font-bold text-indigo-800 mb-4">1. Calculer l'espérance et la variance de la variable Z</h3>
              
              <div className="ml-6 space-y-4">
                <div className="bg-blue-50 p-4 rounded-lg">
                  <p className="font-semibold text-blue-900 mb-2">Étape 1: Calculer E(X)</p>
                  <p>E(X) = Σ xᵢ × P(X = xᵢ)</p>
                  <p>E(X) = 1 × p + (-1) × q + 0 × (1-p-q)</p>
                  <p className="font-bold text-blue-900 mt-2">E(X) = p - q</p>
                </div>

                <div className="bg-blue-50 p-4 rounded-lg">
                  <p className="font-semibold text-blue-900 mb-2">Étape 2: Calculer E(Y)</p>
                  <p>Y a la même loi que X, donc:</p>
                  <p className="font-bold text-blue-900">E(Y) = p - q</p>
                </div>

                <div className="bg-green-50 p-4 rounded-lg border-2 border-green-300">
                  <p className="font-semibold text-green-900 mb-2">✓ Résultat E(Z):</p>
                  <p>Z = X + Y</p>
                  <p>E(Z) = E(X + Y) = E(X) + E(Y)  (car X et Y indépendantes)</p>
                  <p className="text-xl font-bold text-green-900 mt-2">E(Z) = 2(p - q)</p>
                </div>

                <div className="bg-blue-50 p-4 rounded-lg mt-6">
                  <p className="font-semibold text-blue-900 mb-2">Étape 3: Calculer V(X)</p>
                  <p>V(X) = E(X²) - [E(X)]²</p>
                  <p className="mt-2">E(X²) = 1² × p + (-1)² × q + 0² × (1-p-q)</p>
                  <p>E(X²) = p + q</p>
                  <p className="mt-2">V(X) = (p + q) - (p - q)²</p>
                  <p>V(X) = p + q - (p² - 2pq + q²)</p>
                  <p className="font-bold text-blue-900 mt-2">V(X) = p + q - p² - q² + 2pq</p>
                </div>

                <div className="bg-blue-50 p-4 rounded-lg">
                  <p className="font-semibold text-blue-900 mb-2">Étape 4: Calculer V(Y)</p>
                  <p>Y a la même loi que X, donc:</p>
                  <p className="font-bold text-blue-900">V(Y) = p + q - p² - q² + 2pq</p>
                </div>

                <div className="bg-green-50 p-4 rounded-lg border-2 border-green-300">
                  <p className="font-semibold text-green-900 mb-2">✓ Résultat V(Z):</p>
                  <p>Z = X + Y</p>
                  <p>V(Z) = V(X + Y) = V(X) + V(Y)  (car X et Y indépendantes)</p>
                  <p className="text-xl font-bold text-green-900 mt-2">V(Z) = 2(p + q - p² - q² + 2pq)</p>
                </div>
              </div>
            </div>

            {/* Question 2 */}
            <div className="mb-8 border-t-2 border-gray-200 pt-6">
              <h3 className="font-bold text-indigo-800 mb-4">2. Quelle la loi de Z?</h3>
              
              <div className="ml-6 space-y-4">
                <p className="text-gray-700">Z = X + Y, où X, Y ∈ {-1, 0, 1}</p>
                <p className="font-semibold">Valeurs possibles de Z: {-2, -1, 0, 1, 2}</p>

                <div className="bg-yellow-50 p-4 rounded-lg">
                  <p className="font-semibold mb-2">Calcul des probabilités:</p>
                  
                  <div className="space-y-3 ml-4">
                    <div>
                      <p className="font-semibold text-indigo-900">P(Z = -2):</p>
                      <p>X = -1 et Y = -1</p>
                      <p>P(Z = -2) = P(X=-1) × P(Y=-1) = q × q = <span className="font-bold">q²</span></p>
                    </div>

                    <div>
                      <p className="font-semibold text-indigo-900">P(Z = -1):</p>
                      <p>(X=-1, Y=0) ou (X=0, Y=-1)</p>
                      <p>P(Z = -1) = q(1-p-q) + (1-p-q)q = <span className="font-bold">2q(1-p-q)</span></p>
                    </div>

                    <div>
                      <p className="font-semibold text-indigo-900">P(Z = 0):</p>
                      <p>(X=-1, Y=1) ou (X=0, Y=0) ou (X=1, Y=-1)</p>
                      <p>P(Z = 0) = pq + (1-p-q)² + qp = <span className="font-bold">2pq + (1-p-q)²</span></p>
                    </div>

                    <div>
                      <p className="font-semibold text-indigo-900">P(Z = 1):</p>
                      <p>(X=1, Y=0) ou (X=0, Y=1)</p>
                      <p>P(Z = 1) = p(1-p-q) + (1-p-q)p = <span className="font-bold">2p(1-p-q)</span></p>
                    </div>

                    <div>
                      <p className="font-semibold text-indigo-900">P(Z = 2):</p>
                      <p>X = 1 et Y = 1</p>
                      <p>P(Z = 2) = p × p = <span className="font-bold">p²</span></p>
                    </div>
                  </div>
                </div>

                <div className="bg-green-50 p-4 rounded-lg border-2 border-green-300">
                  <p className="font-bold text-green-900 mb-3">✓ Loi de Z:</p>
                  <table className="w-full border-collapse border-2 border-green-300">
                    <thead>
                      <tr className="bg-green-200">
                        <th className="border border-green-300 p-2">Z</th>
                        <th className="border border-green-300 p-2">-2</th>
                        <th className="border border-green-300 p-2">-1</th>
                        <th className="border border-green-300 p-2">0</th>
                        <th className="border border-green-300 p-2">1</th>
                        <th className="border border-green-300 p-2">2</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td className="border border-green-300 p-2 font-semibold">P(Z)</td>
                        <td className="border border-green-300 p-2">q²</td>
                        <td className="border border-green-300 p-2">2q(1-p-q)</td>
                        <td className="border border-green-300 p-2">2pq+(1-p-q)²</td>
                        <td className="border border-green-300 p-2">2p(1-p-q)</td>
                        <td className="border border-green-300 p-2">p²</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>
            </div>

            {/* Question 3 */}
            <div className="mb-8 border-t-2 border-gray-200 pt-6">
              <h3 className="font-bold text-indigo-800 mb-4">3. Calculer P(Z {'>'} 0), P(Z = 0), et P(Z {'<'} 0)</h3>
              
              <div className="ml-6 space-y-4">
                <div className="bg-blue-50 p-4 rounded-lg">
                  <p className="font-semibold text-blue-900 mb-2">P(Z {'>'} 0):</p>
                  <p>P(Z {'>'} 0) = P(Z=1) + P(Z=2)</p>
                  <p>P(Z {'>'} 0) = 2p(1-p-q) + p²</p>
                  <p className="font-bold text-xl text-blue-900 mt-2">P(Z {'>'} 0) = 2p - 2p² - 2pq + p² = p(2 - p - 2q)</p>
                </div>

                <div className="bg-blue-50 p-4 rounded-lg">
                  <p className="font-semibold text-blue-900 mb-2">P(Z = 0):</p>
                  <p className="font-bold text-xl text-blue-900">P(Z = 0) = 2pq + (1-p-q)²</p>
                </div>

                <div className="bg-blue-50 p-4 rounded-lg">
                  <p className="font-semibold text-blue-900 mb-2">P(Z {'<'} 0):</p>
                  <p>P(Z {'<'} 0) = P(Z=-2) + P(Z=-1)</p>
                  <p>P(Z {'<'} 0) = q² + 2q(1-p-q)</p>
                  <p className="font-bold text-xl text-blue-900 mt-2">P(Z {'<'} 0) = q(2 - q - 2p)</p>
                </div>

                <div className="bg-green-50 p-4 rounded-lg border-2 border-green-300 mt-4">
                  <p className="font-semibold text-green-900">✓ Vérification:</p>
                  <p>P(Z{'<'}0) + P(Z=0) + P(Z{'>'}0) = 1 ✓</p>
                </div>
              </div>
            </div>
          </div>

          {/* Exercice 6 */}
          <div className="page-break-before">
            <h2 className="text-2xl font-bold text-indigo-900 mb-6 pb-2 border-b-2 border-indigo-200">
              Exercice 6
            </h2>

            <div className="bg-gray-50 p-6 rounded-lg mb-6">
              <h3 className="font-bold text-lg mb-3">📋 Énoncé:</h3>
              <p>Démontrer les propriétés suivantes pour différentes lois de probabilité:</p>
            </div>

            {/* Question 1 */}
            <div className="mb-8">
              <h3 className="font-bold text-indigo-800 mb-4">1. Si X ↪ B(n,p) montrer que: E(X) = np et V(X) = npq</h3>
              
              <div className="ml-6 space-y-4">
                <div className="bg-yellow-50 p-4 rounded-lg">
                  <p className="font-semibold mb-2">Rappel: Loi Binomiale</p>
                  <p>X ~ B(n,p) signifie qu'on répète n fois une expérience de Bernoulli avec probabilité de succès p</p>
                  <p>X = nombre de succès sur n essais</p>
                  <p>q = 1 - p (probabilité d'échec)</p>
                </div>

                <div className="bg-blue-50 p-4 rounded-lg">
                  <p className="font-semibold text-blue-900 mb-3">Démonstration de E(X) = np:</p>
                  <p>On peut écrire X = X₁ + X₂ + ... + Xₙ</p>
                  <p>où chaque Xᵢ ~ B(1,p) (Bernoulli)</p>
                  <p className="mt-2">Pour une Bernoulli: E(Xᵢ) = 0×(1-p) + 1×p = p</p>
                  <p className="mt-2">Par linéarité de l'espérance:</p>
                  <p>E(X) = E(X₁ + X₂ + ... + Xₙ)</p>
                  <p>E(X) = E(X₁) + E(X₂) + ... + E(Xₙ)</p>
                  <p className="font-bold text-xl text-blue-900 mt-2">E(X) = n × p = np ✓</p>
                </div>

                <div className="bg-blue-50 p-4 rounded-lg">
                  <p className="font-semibold text-blue-900 mb-3">Démonstration de V(X) = npq:</p>
                  <p>Pour une Bernoulli Xᵢ:</p>
                  <p>E(Xᵢ²) = 0²×(1-p) + 1²×p = p</p>
                  <p>V(Xᵢ) = E(Xᵢ²) - [E(Xᵢ)]² = p - p² = p(1-p) = pq</p>
                  <p className="mt-3">Comme X₁, X₂, ..., Xₙ sont indépendantes:</p>
                  <p>V(X) = V(X₁ + X₂ + ... + Xₙ)</p>
                  <p>V(X) = V(X₁) + V(X₂) + ... + V(Xₙ)</p>
                  <p className="font-bold text-xl text-blue-900 mt-2">V(X) = n × pq = npq ✓</p>
                </div>
              </div>
            </div>

            {/* Question 2 */}
            <div className="mb-8 border-t-2 border-gray-200 pt-6">
              <h3 className="font-bold text-indigo-800 mb-4">2. Si X ↪ P(λ) montrer que: E(X) = λ et V(X) = λ</h3>
              
              <div className="ml-6 space-y-4">
                <div className="bg-yellow-50 p-4 rounded-lg">
                  <p className="font-semibold mb-2">Rappel: Loi de Poisson</p>
                  <p>X ~ P(λ) avec P(X = k) = (λᵏ × e⁻λ) / k!</p>
                  <p>où λ {'>'} 0 est le paramètre d'intensité</p>
                </div>

                <div className="bg-blue-50 p-4 rounded-lg">
                  <p className="font-semibold text-blue-900 mb-3">Démonstration de E(X) = λ:</p>
                  <p>E(X) = Σ k × P(X=k) = Σ k × (λᵏe⁻λ)/k!</p>
                  <p className="mt-2">E(X) = Σ(k=1 à ∞) k × (λᵏe⁻λ)/k!</p>
                  <p>E(X) = Σ(k=1 à ∞) (λᵏe⁻λ)/(k-1)!</p>
                  <p>E(X) = λe⁻λ × Σ(k=1 à ∞) λᵏ⁻¹/(k-1)!</p>
                  <p className="mt-2">En posant j = k-1:</p>
                  <p>E(X) = λe⁻λ × Σ(j=0 à ∞) λʲ/j!</p>
                  <p>E(X) = λe⁻λ × eλ</p>
                  <p className="font-bold text-xl text-blue-900 mt-2">E(X) = λ ✓</p>
                </div>

                <div className="bg-blue-50 p-4 rounded-lg">
                  <p className="font-semibold text-blue-900 mb-3">Démonstration de V(X) = λ:</p>
                  <p>V(X) = E(X²) - [E(X)]²</p>
                  <p className="mt-2">Calculons E(X²) = E[X(X-1)] + E(X):</p>
                  <p>E[X(X-1)] = Σ k(k-1) × (λᵏe⁻λ)/k!</p>
                  <p>E[X(X-1)] = Σ(k=2 à ∞) (λᵏe⁻λ)/(k-2)!</p>
                  <p>E[X(X-1)] = λ²e⁻λ × eλ = λ²</p>
                  <p className="mt-2">Donc: E(X²) = λ² + λ</p>
                  <p>V(X) = (λ² + λ) - λ²</p>
                  <p className="font-bold text-xl text-blue-900 mt-2">V(X) = λ ✓</p>
                </div>

                <div className="bg-green-50 p-4 rounded-lg border-2 border-green-300">
                  <p className="font-semibold text-green-900">✓ Propriété remarquable de Poisson:</p>
                  <p className="text-lg">Pour la loi de Poisson, l'espérance égale la variance!</p>
                </div>
              </div>
            </div>

            {/* Question 3 */}
            <div className="mb-8 border-t-2 border-gray-200 pt-6">
              <h3 className="font-bold text-indigo-800 mb-4">3. Si X ↪ G(p) montrer que: E(X) = 1/p et V(X) = (1-p)/p²</h3>
              
              <div className="ml-6 space-y-4">
                <div className="bg-yellow-50 p-4 rounded-lg">
                  <p className="font-semibold mb-2">Rappel: Loi Géométrique</p>
                  <p>X ~ G(p) représente le nombre d'essais avant le premier succès</p>
                  <p>P(X = k) = (1-p)ᵏ⁻¹ × p pour k ≥ 1</p>
                  <p>q = 1 - p</p>
                </div>

                <div className="bg-blue-50 p-4 rounded-lg">
                  <p className="font-semibold text-blue-900 mb-3">Démonstration de E(X) = 1/p:</p>
                  <p>E(X) = Σ(k=1 à ∞) k × qᵏ⁻¹ × p</p>
                  <p>E(X) = p × Σ(k=1 à ∞) k × qᵏ⁻¹</p>
                  <p className="mt-2">On sait que: Σ(k=1 à ∞) k × xᵏ⁻¹ = 1/(1-x)² pour |x| {'<'} 1</p>
                  <p>E(X) = p × 1/(1-q)²</p>
                  <p>E(X) = p × 1/p²</p>
                  <p className="font-bold text-xl text-blue-900 mt-2">E(X) = 1/p ✓</p>
                </div>

                <div className="bg-blue-50 p-4 rounded-lg">
                  <p className="font-semibold text-blue-900 mb-3">Démonstration de V(X) = (1-p)/p²:</p>
                  <p>V(X) = E(X²) - [E(X)]²</p>
                  <p className="mt-2">Calculons E(X²):</p>
                  <p>E(X²) = Σ(k=1 à ∞) k² × qᵏ⁻¹ × p</p>
                  <p>E(X²) = p × Σ(k=1 à ∞) k² × qᵏ⁻¹</p>
                  <p className="mt-2">En utilisant: Σ k²xᵏ⁻¹ = (1+x)/(1-x)³</p>
                  <p>E(X²) = p × (1+q)/(1-q)³ = p × (1+q)/p³ = (1+q)/p²</p>
                  <p className="mt-2">V(X) = (1+q)/p² - 1/p²</p>
                  <p>V(X) = q/p²</p>
                  <p className="font-bold text-xl text-blue-900 mt-2">V(X) = (1-p)/p² ✓</p>
                </div>
              </div>
            </div>
          </div>

          {/* Footer */}
          <div className="mt-12 pt-6 border-t-2 border-gray-300 text-center text-gray-600">
            <p>Solutions complètes - TD 2 Probabilité</p>
            <p className="text-sm mt-2">ENSAM Mohammedia - Année 2024/2025</p>
          </div>
        </div>
      </div>

      <style jsx>{`
        @media print {
          .page-break-before {
            page-break-before: always;
          }
        }
      `}</style>
    </div>
  );
};

export default ProbabilityExercises;
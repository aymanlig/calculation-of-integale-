
import math
import re
from typing import Optional, Tuple, List


# ═══════════════════════════════════════════════════════════════
#  SECTION 0: JADWAL DYL DÉVELOPPEMENTS LIMITÉS (Taylor Series)
# ═══════════════════════════════════════════════════════════════

class JadwalDL:
    """
    Jadwal = Table | DL = Développement Limité (Taylor/Maclaurin Series)
    
    Hna kandir les développements limités me3rufin:
    - e^x, sin(x), cos(x), tan(x), ln(1+x), arctan(x), etc.
    - (1+x)^a, 1/(1+x), 1/(1-x), sqrt(1+x), etc.
    - sinh(x), cosh(x), tanh(x)
    
    Kol DL 3andu:
      - silsila_ramziya: the symbolic series string
      - silsila_hadd: function that computes n-th term
      - nitaq_taqarob: radius of convergence
    """

    @staticmethod
    def dl_exp(muta8ayir='x', daraja=10, mu3amil_a=1):
        """
        DL dyal e^(ax):
        e^(ax) = Σ (ax)^n / n!  = 1 + ax + (ax)^2/2! + (ax)^3/3! + ...
        Nitaq (Radius): ∞
        """
        silsila_huruf = f"DL(e^({mu3amil_a}{muta8ayir})) = "
        hudud = []  # hudud = terms
        for n in range(daraja + 1):
            if mu3amil_a == 1:
                if n == 0:
                    hudud.append("1")
                elif n == 1:
                    hudud.append(f"{muta8ayir}")
                else:
                    hudud.append(f"{muta8ayir}^{n}/{math.factorial(n)}")
            else:
                a_power = mu3amil_a ** n
                if n == 0:
                    hudud.append("1")
                elif n == 1:
                    hudud.append(f"{a_power}*{muta8ayir}")
                else:
                    mu3amil = a_power / math.factorial(n)
                    hudud.append(f"{mu3amil:.6g}*{muta8ayir}^{n}")
        silsila_huruf += " + ".join(hudud) + " + ..."
        
        def hadd_n(x_qima, n):
            """Compute n-th term at x = x_qima"""
            return (mu3amil_a * x_qima) ** n / math.factorial(n)
        
        nitaq = float('inf')
        return silsila_huruf, hadd_n, nitaq, daraja

    @staticmethod
    def dl_sin(muta8ayir='x', daraja=10, mu3amil_a=1):
        """
        DL dyal sin(ax):
        sin(ax) = Σ (-1)^n * (ax)^(2n+1) / (2n+1)!
               = ax - (ax)^3/3! + (ax)^5/5! - ...
        Nitaq: ∞
        """
        silsila_huruf = f"DL(sin({mu3amil_a}{muta8ayir})) = "
        hudud = []
        for n in range(daraja + 1):
            qowa = 2 * n + 1  # power = 2n+1
            ishara = (-1) ** n  # sign alternates
            maqam = math.factorial(qowa)  # denominator
            a_power = mu3amil_a ** qowa
            mu3amil = ishara * a_power / maqam
            if n == 0:
                if mu3amil_a == 1:
                    hudud.append(f"{muta8ayir}")
                else:
                    hudud.append(f"{mu3amil_a}*{muta8ayir}")
            else:
                hudud.append(f"{mu3amil:.6g}*{muta8ayir}^{qowa}")
        silsila_huruf += " + ".join(hudud) + " + ..."
        
        def hadd_n(x_qima, n):
            qowa = 2 * n + 1
            return ((-1) ** n) * ((mu3amil_a * x_qima) ** qowa) / math.factorial(qowa)
        
        nitaq = float('inf')
        return silsila_huruf, hadd_n, nitaq, daraja

    @staticmethod
    def dl_cos(muta8ayir='x', daraja=10, mu3amil_a=1):
        """
        DL dyal cos(ax):
        cos(ax) = Σ (-1)^n * (ax)^(2n) / (2n)!
               = 1 - (ax)^2/2! + (ax)^4/4! - ...
        Nitaq: ∞
        """
        silsila_huruf = f"DL(cos({mu3amil_a}{muta8ayir})) = "
        hudud = []
        for n in range(daraja + 1):
            qowa = 2 * n
            ishara = (-1) ** n
            maqam = math.factorial(qowa)
            a_power = mu3amil_a ** qowa
            mu3amil = ishara * a_power / maqam
            if n == 0:
                hudud.append("1")
            else:
                hudud.append(f"{mu3amil:.6g}*{muta8ayir}^{qowa}")
        silsila_huruf += " + ".join(hudud) + " + ..."
        
        def hadd_n(x_qima, n):
            qowa = 2 * n
            return ((-1) ** n) * ((mu3amil_a * x_qima) ** qowa) / math.factorial(qowa)
        
        nitaq = float('inf')
        return silsila_huruf, hadd_n, nitaq, daraja

    @staticmethod
    def dl_tan(muta8ayir='x', daraja=7):
        """
        DL dyal tan(x):
        tan(x) = x + x^3/3 + 2x^5/15 + 17x^7/315 + ...
        Nitaq: |x| < π/2
        
        Bernoulli numbers based coefficients (hardcoded first terms)
        """
        # Mu3amilat me3rufin dyal tan(x) Taylor
        mu3amilat_tan = {
            1: 1.0,
            3: 1.0 / 3,
            5: 2.0 / 15,
            7: 17.0 / 315,
            9: 62.0 / 2835,
            11: 1382.0 / 155925,
            13: 21844.0 / 6081075
        }
        
        silsila_huruf = f"DL(tan({muta8ayir})) = "
        hudud = []
        for qowa, mu3amil in mu3amilat_tan.items():
            if qowa > daraja * 2 + 1:
                break
            if qowa == 1:
                hudud.append(f"{muta8ayir}")
            else:
                hudud.append(f"{mu3amil:.6g}*{muta8ayir}^{qowa}")
        silsila_huruf += " + ".join(hudud) + " + ..."
        
        def hadd_n(x_qima, n):
            qowa = 2 * n + 1
            if qowa in mu3amilat_tan:
                return mu3amilat_tan[qowa] * (x_qima ** qowa)
            return 0.0
        
        nitaq = math.pi / 2
        return silsila_huruf, hadd_n, nitaq, daraja

    @staticmethod
    def dl_ln_1_plus_x(muta8ayir='x', daraja=10):
        """
        DL dyal ln(1+x):
        ln(1+x) = Σ (-1)^(n+1) * x^n / n  (n=1 to ∞)
                = x - x^2/2 + x^3/3 - x^4/4 + ...
        Nitaq: -1 < x ≤ 1
        """
        silsila_huruf = f"DL(ln(1+{muta8ayir})) = "
        hudud = []
        for n in range(1, daraja + 1):
            ishara = (-1) ** (n + 1)
            mu3amil = ishara / n
            if n == 1:
                hudud.append(f"{muta8ayir}")
            else:
                hudud.append(f"{mu3amil:.6g}*{muta8ayir}^{n}")
        silsila_huruf += " + ".join(hudud) + " + ..."
        
        def hadd_n(x_qima, n):
            if n == 0:
                return 0.0
            return ((-1) ** (n + 1)) * (x_qima ** n) / n
        
        nitaq = 1.0
        return silsila_huruf, hadd_n, nitaq, daraja

    @staticmethod
    def dl_ln_1_minus_x(muta8ayir='x', daraja=10):
        """
        DL dyal ln(1-x):
        ln(1-x) = -Σ x^n / n  (n=1 to ∞)
                = -x - x^2/2 - x^3/3 - ...
        Nitaq: -1 ≤ x < 1
        """
        silsila_huruf = f"DL(ln(1-{muta8ayir})) = "
        hudud = []
        for n in range(1, daraja + 1):
            mu3amil = -1.0 / n
            if n == 1:
                hudud.append(f"-{muta8ayir}")
            else:
                hudud.append(f"{mu3amil:.6g}*{muta8ayir}^{n}")
        silsila_huruf += " + ".join(hudud) + " + ..."
        
        def hadd_n(x_qima, n):
            if n == 0:
                return 0.0
            return -(x_qima ** n) / n
        
        nitaq = 1.0
        return silsila_huruf, hadd_n, nitaq, daraja

    @staticmethod
    def dl_arctan(muta8ayir='x', daraja=10):
        """
        DL dyal arctan(x):
        arctan(x) = Σ (-1)^n * x^(2n+1) / (2n+1)
                  = x - x^3/3 + x^5/5 - x^7/7 + ...
        Nitaq: |x| ≤ 1
        """
        silsila_huruf = f"DL(arctan({muta8ayir})) = "
        hudud = []
        for n in range(daraja + 1):
            qowa = 2 * n + 1
            ishara = (-1) ** n
            mu3amil = ishara / qowa
            if n == 0:
                hudud.append(f"{muta8ayir}")
            else:
                hudud.append(f"{mu3amil:.6g}*{muta8ayir}^{qowa}")
        silsila_huruf += " + ".join(hudud) + " + ..."
        
        def hadd_n(x_qima, n):
            qowa = 2 * n + 1
            return ((-1) ** n) * (x_qima ** qowa) / qowa
        
        nitaq = 1.0
        return silsila_huruf, hadd_n, nitaq, daraja

    @staticmethod
    def dl_arcsin(muta8ayir='x', daraja=10):
        """
        DL dyal arcsin(x):
        arcsin(x) = Σ (2n)! / (4^n * (n!)^2 * (2n+1)) * x^(2n+1)
                  = x + x^3/6 + 3x^5/40 + 15x^7/336 + ...
        Nitaq: |x| ≤ 1
        """
        silsila_huruf = f"DL(arcsin({muta8ayir})) = "
        hudud = []
        for n in range(daraja + 1):
            qowa = 2 * n + 1
            bast = math.factorial(2 * n)  # numerator part
            maqam = (4 ** n) * (math.factorial(n) ** 2) * qowa
            mu3amil = bast / maqam
            if n == 0:
                hudud.append(f"{muta8ayir}")
            else:
                hudud.append(f"{mu3amil:.6g}*{muta8ayir}^{qowa}")
        silsila_huruf += " + ".join(hudud) + " + ..."
        
        def hadd_n(x_qima, n):
            qowa = 2 * n + 1
            bast = math.factorial(2 * n)
            maqam = (4 ** n) * (math.factorial(n) ** 2) * qowa
            return (bast / maqam) * (x_qima ** qowa)
        
        nitaq = 1.0
        return silsila_huruf, hadd_n, nitaq, daraja

    @staticmethod
    def dl_1_plus_x_power_a(mu3amil_a, muta8ayir='x', daraja=10):
        """
        DL dyal (1+x)^a  (Binomial Series):
        (1+x)^a = Σ C(a,n) * x^n
                = 1 + a*x + a(a-1)/2! * x^2 + a(a-1)(a-2)/3! * x^3 + ...
        Nitaq: |x| < 1 (when a is not a non-negative integer)
        """
        silsila_huruf = f"DL((1+{muta8ayir})^{mu3amil_a}) = "
        hudud = []
        
        def binomial_coeff(a_val, n_val):
            """C(a, n) = a*(a-1)*...*(a-n+1) / n!"""
            if n_val == 0:
                return 1.0
            natija_j = 1.0
            for i in range(n_val):
                natija_j *= (a_val - i)
            natija_j /= math.factorial(n_val)
            return natija_j
        
        for n in range(daraja + 1):
            mu3amil = binomial_coeff(mu3amil_a, n)
            if n == 0:
                hudud.append("1")
            elif n == 1:
                hudud.append(f"{mu3amil:.6g}*{muta8ayir}")
            else:
                hudud.append(f"{mu3amil:.6g}*{muta8ayir}^{n}")
        silsila_huruf += " + ".join(hudud) + " + ..."
        
        def hadd_n(x_qima, n):
            return binomial_coeff(mu3amil_a, n) * (x_qima ** n)
        
        nitaq = 1.0 if not (isinstance(mu3amil_a, int) and mu3amil_a >= 0) else float('inf')
        return silsila_huruf, hadd_n, nitaq, daraja

    @staticmethod
    def dl_1_over_1_plus_x(muta8ayir='x', daraja=10):
        """
        DL dyal 1/(1+x) = (1+x)^(-1):
        1/(1+x) = Σ (-1)^n * x^n = 1 - x + x^2 - x^3 + ...
        Nitaq: |x| < 1
        """
        return JadwalDL.dl_1_plus_x_power_a(-1, muta8ayir, daraja)

    @staticmethod
    def dl_1_over_1_minus_x(muta8ayir='x', daraja=10):
        """
        DL dyal 1/(1-x):
        1/(1-x) = Σ x^n = 1 + x + x^2 + x^3 + ...  (Geometric Series)
        Nitaq: |x| < 1
        """
        silsila_huruf = f"DL(1/(1-{muta8ayir})) = "
        hudud = []
        for n in range(daraja + 1):
            if n == 0:
                hudud.append("1")
            elif n == 1:
                hudud.append(f"{muta8ayir}")
            else:
                hudud.append(f"{muta8ayir}^{n}")
        silsila_huruf += " + ".join(hudud) + " + ..."
        
        def hadd_n(x_qima, n):
            return x_qima ** n
        
        nitaq = 1.0
        return silsila_huruf, hadd_n, nitaq, daraja

    @staticmethod
    def dl_sqrt_1_plus_x(muta8ayir='x', daraja=10):
        """
        DL dyal √(1+x) = (1+x)^(1/2):
        √(1+x) = 1 + x/2 - x^2/8 + x^3/16 - ...
        Nitaq: |x| < 1
        """
        return JadwalDL.dl_1_plus_x_power_a(0.5, muta8ayir, daraja)

    @staticmethod
    def dl_1_over_sqrt_1_plus_x(muta8ayir='x', daraja=10):
        """
        DL dyal 1/√(1+x) = (1+x)^(-1/2):
        Nitaq: |x| < 1
        """
        return JadwalDL.dl_1_plus_x_power_a(-0.5, muta8ayir, daraja)

    @staticmethod
    def dl_sinh(muta8ayir='x', daraja=10):
        """
        DL dyal sinh(x):
        sinh(x) = Σ x^(2n+1) / (2n+1)!
                = x + x^3/3! + x^5/5! + ...
        Nitaq: ∞
        """
        silsila_huruf = f"DL(sinh({muta8ayir})) = "
        hudud = []
        for n in range(daraja + 1):
            qowa = 2 * n + 1
            mu3amil = 1.0 / math.factorial(qowa)
            if n == 0:
                hudud.append(f"{muta8ayir}")
            else:
                hudud.append(f"{mu3amil:.6g}*{muta8ayir}^{qowa}")
        silsila_huruf += " + ".join(hudud) + " + ..."
        
        def hadd_n(x_qima, n):
            qowa = 2 * n + 1
            return (x_qima ** qowa) / math.factorial(qowa)
        
        nitaq = float('inf')
        return silsila_huruf, hadd_n, nitaq, daraja

    @staticmethod
    def dl_cosh(muta8ayir='x', daraja=10):
        """
        DL dyal cosh(x):
        cosh(x) = Σ x^(2n) / (2n)!
                = 1 + x^2/2! + x^4/4! + ...
        Nitaq: ∞
        """
        silsila_huruf = f"DL(cosh({muta8ayir})) = "
        hudud = []
        for n in range(daraja + 1):
            qowa = 2 * n
            mu3amil = 1.0 / math.factorial(qowa)
            if n == 0:
                hudud.append("1")
            else:
                hudud.append(f"{mu3amil:.6g}*{muta8ayir}^{qowa}")
        silsila_huruf += " + ".join(hudud) + " + ..."
        
        def hadd_n(x_qima, n):
            qowa = 2 * n
            return (x_qima ** qowa) / math.factorial(qowa)
        
        nitaq = float('inf')
        return silsila_huruf, hadd_n, nitaq, daraja

    @staticmethod
    def dl_tanh(muta8ayir='x', daraja=7):
        """
        DL dyal tanh(x):
        tanh(x) = x - x^3/3 + 2x^5/15 - 17x^7/315 + ...
        Nitaq: |x| < π/2
        """
        mu3amilat_tanh = {
            1: 1.0,
            3: -1.0 / 3,
            5: 2.0 / 15,
            7: -17.0 / 315,
            9: 62.0 / 2835,
            11: -1382.0 / 155925,
        }
        
        silsila_huruf = f"DL(tanh({muta8ayir})) = "
        hudud = []
        for qowa, mu3amil in mu3amilat_tanh.items():
            if qowa > daraja * 2 + 1:
                break
            if qowa == 1:
                hudud.append(f"{muta8ayir}")
            else:
                hudud.append(f"{mu3amil:.6g}*{muta8ayir}^{qowa}")
        silsila_huruf += " + ".join(hudud) + " + ..."
        
        def hadd_n(x_qima, n):
            qowa = 2 * n + 1
            if qowa in mu3amilat_tanh:
                return mu3amilat_tanh[qowa] * (x_qima ** qowa)
            return 0.0
        
        nitaq = math.pi / 2
        return silsila_huruf, hadd_n, nitaq, daraja

    @staticmethod
    def dl_log_x(muta8ayir='x', markaz=1, daraja=10):
        """
        DL dyal ln(x) around x=a (Taylor expansion about a=1):
        ln(x) = ln(a) + Σ (-1)^(n+1) * (x-a)^n / (n * a^n)
        For a=1: ln(x) = (x-1) - (x-1)^2/2 + (x-1)^3/3 - ...
        = same as ln(1+u) where u = x-1
        """
        if markaz == 1:
            silsila_huruf = f"DL(ln({muta8ayir})) [around {muta8ayir}=1] = "
            hudud = []
            for n in range(1, daraja + 1):
                ishara = (-1) ** (n + 1)
                mu3amil = ishara / n
                if n == 1:
                    hudud.append(f"({muta8ayir}-1)")
                else:
                    hudud.append(f"{mu3amil:.6g}*({muta8ayir}-1)^{n}")
            silsila_huruf += " + ".join(hudud) + " + ..."
            
            def hadd_n(x_qima, n):
                if n == 0:
                    return 0.0
                u = x_qima - 1
                return ((-1) ** (n + 1)) * (u ** n) / n
            
            nitaq = 1.0
            return silsila_huruf, hadd_n, nitaq, daraja
        else:
            return JadwalDL.dl_ln_1_plus_x(muta8ayir, daraja)

    @staticmethod
    def dl_e_power_minus_x_sq(muta8ayir='x', daraja=10):
        """
        DL dyal e^(-x²):
        e^(-x²) = Σ (-1)^n * x^(2n) / n!
                = 1 - x² + x⁴/2! - x⁶/3! + ...
        Nitaq: ∞
        Muhim l'intégrale de Gauss!
        """
        silsila_huruf = f"DL(e^(-{muta8ayir}²)) = "
        hudud = []
        for n in range(daraja + 1):
            qowa = 2 * n
            ishara = (-1) ** n
            mu3amil = ishara / math.factorial(n)
            if n == 0:
                hudud.append("1")
            else:
                hudud.append(f"{mu3amil:.6g}*{muta8ayir}^{qowa}")
        silsila_huruf += " + ".join(hudud) + " + ..."
        
        def hadd_n(x_qima, n):
            qowa = 2 * n
            return ((-1) ** n) * (x_qima ** qowa) / math.factorial(n)
        
        nitaq = float('inf')
        return silsila_huruf, hadd_n, nitaq, daraja

    @staticmethod
    def dl_arcsin_extended(muta8ayir='x', daraja=10):
        """Same as dl_arcsin but alias for clarity"""
        return JadwalDL.dl_arcsin(muta8ayir, daraja)

    @staticmethod
    def hesab_dl(hadd_func, x_qima, daraja):
        """
        Compute the value of DL at a specific x.
        hesab = compute | qima = value
        """
        majmu3 = 0.0  # sum
        for n in range(daraja + 1):
            majmu3 += hadd_func(x_qima, n)
        return majmu3

    @staticmethod
    def takamol_dl(hadd_func, bidaya, nihaya, daraja):
        """
        Integrate the DL term by term!
        ∫ Σ a_n * x^n dx = Σ a_n * x^(n+1)/(n+1)
        
        This is the KEY connection: use DL to solve hard integrals
        by integrating the series term by term.
        """
        from functools import partial
        
        def hadd_takamol(x_qima, n, hadd_f):
            """
            Approximate integral of n-th term from 0 to x
            Using the original term and numerical micro-integration
            """
            khatawat = 100
            dx = x_qima / khatawat if khatawat > 0 else 0
            majmu3 = 0.0
            for i in range(khatawat):
                xi = (i + 0.5) * dx
                majmu3 += hadd_f(xi, n) * dx
            return majmu3
        
        natija_takamol = 0.0
        for n in range(daraja + 1):
            qima_b = hadd_takamol(nihaya, n, hadd_func)
            qima_a = hadd_takamol(bidaya, n, hadd_func)
            natija_takamol += (qima_b - qima_a)
        return natija_takamol

    @staticmethod
    def ard_kol_dl():
        """Display all available DL formulas - ard = display, kol = all"""
        khat = "═" * 60
        print(f"\n{khat}")
        print("  📚 JADWAL KAMIL DYL DÉVELOPPEMENTS LIMITÉS")
        print(f"{khat}")
        
        qa2imat_dl = [
            ("e^x", JadwalDL.dl_exp, {}),
            ("sin(x)", JadwalDL.dl_sin, {}),
            ("cos(x)", JadwalDL.dl_cos, {}),
            ("tan(x)", JadwalDL.dl_tan, {}),
            ("ln(1+x)", JadwalDL.dl_ln_1_plus_x, {}),
            ("ln(1-x)", JadwalDL.dl_ln_1_minus_x, {}),
            ("arctan(x)", JadwalDL.dl_arctan, {}),
            ("arcsin(x)", JadwalDL.dl_arcsin, {}),
            ("(1+x)^a [a=0.5]", JadwalDL.dl_1_plus_x_power_a, {'mu3amil_a': 0.5}),
            ("1/(1+x)", JadwalDL.dl_1_over_1_plus_x, {}),
            ("1/(1-x)", JadwalDL.dl_1_over_1_minus_x, {}),
            ("√(1+x)", JadwalDL.dl_sqrt_1_plus_x, {}),
            ("1/√(1+x)", JadwalDL.dl_1_over_sqrt_1_plus_x, {}),
            ("sinh(x)", JadwalDL.dl_sinh, {}),
            ("cosh(x)", JadwalDL.dl_cosh, {}),
            ("tanh(x)", JadwalDL.dl_tanh, {}),
            ("e^(-x²)", JadwalDL.dl_e_power_minus_x_sq, {}),
        ]
        
        for ism, func, kwargs in qa2imat_dl:
            try:
                s, _, nitaq, _ = func(daraja=5, **kwargs)
                print(f"\n  📌 {ism}")
                print(f"     {s}")
                print(f"     Nitaq t-taqarob (Radius): {nitaq}")
            except Exception as kh:
                print(f"\n  📌 {ism} - Khata2: {kh}")
        
        print(f"\n{khat}\n")


# ═══════════════════════════════════════════════════════════════
#  SECTION 1: TURUQ MUTAQADDIMA (Advanced Mathematical Tricks)
# ═══════════════════════════════════════════════════════════════

class TuruqMutaqaddima:
    """
    Turuq = Methods | Mutaqaddima = Advanced
    
    Hna kandir les techniques avancées li kaysta3mluhum mathematicians:
    
    1. Takamol b-l-ajza2 (Integration by Parts): ∫u dv = uv - ∫v du
    2. Ta8yir l-muta8ayir (Substitution / u-substitution)
    3. Tajzi2a ila kusur juz2iya (Partial Fractions)
    4. Ta8yir trigonométrique (Trig Substitution)
    5. Takamol Weierstrass (t = tan(x/2))
    6. Takamol b-DL (Integration via Taylor Series)
    7. Takamol Feynman (Differentiation under integral sign)
    8. Formules de réduction (Reduction formulas)
    """

    @staticmethod
    def takamol_ajza2(u_str, dv_str, muta8ayir='x'):
        """
        Integration by Parts: ∫u dv = uv - ∫v du
        
        Tabular method (LIATE rule):
        L - Logarithmic
        I - Inverse trig
        A - Algebraic (polynomial)
        T - Trigonometric
        E - Exponential
        
        Returns description of the process.
        """
        sharh = []  # sharh = explanation
        sharh.append(f"  ⚙️ Takamol b-l-ajza2 (Integration by Parts)")
        sharh.append(f"     ∫ {u_str} · d({dv_str})")
        sharh.append(f"     = {u_str} · {dv_str} - ∫ {dv_str} · d({u_str})")
        sharh.append(f"     (Qa3idat LIATE: Log > InvTrig > Algebraic > Trig > Exp)")
        return "\n".join(sharh)

    @staticmethod
    def ta8yir_muta8ayir_sharh(mo3adala, ta8yir, muta8ayir='x'):
        """
        u-Substitution explanation:
        If we let u = g(x), then du = g'(x)dx
        ∫f(g(x))·g'(x)dx = ∫f(u)du
        """
        sharh = []
        sharh.append(f"  ⚙️ Ta8yir l-muta8ayir (Substitution)")
        sharh.append(f"     Mo3adala: ∫ {mo3adala} d{muta8ayir}")
        sharh.append(f"     Nkhtar: u = {ta8yir}")
        sharh.append(f"     => du = d({ta8yir})")
        sharh.append(f"     Nbeddel f l-integral o nhel b u")
        return "\n".join(sharh)

    @staticmethod
    def kusur_juz2iya(bast, maqam_factors):
        """
        Partial Fractions Decomposition:
        P(x)/Q(x) = A/(x-a) + B/(x-b) + ...
        
        bast = numerator | maqam = denominator
        maqam_factors = list of (root, multiplicity)
        """
        sharh = []
        sharh.append(f"  ⚙️ Tajzi2a ila Kusur Juz2iya (Partial Fractions)")
        sharh.append(f"     Bast (Numerator): {bast}")
        sharh.append(f"     Maqam factors: {maqam_factors}")
        
        qism_juz2i = []
        harf = ord('A')
        for jidr, ta3addud in maqam_factors:
            for k in range(1, ta3addud + 1):
                mu3amil_harf = chr(harf)
                harf += 1
                if k == 1:
                    qism_juz2i.append(f"{mu3amil_harf}/(x-({jidr}))")
                else:
                    qism_juz2i.append(f"{mu3amil_harf}/(x-({jidr}))^{k}")
        
        sharh.append(f"     = {' + '.join(qism_juz2i)}")
        sharh.append(f"     Kol ∫A/(x-a) = A·ln|x-a|")
        sharh.append(f"     Kol ∫A/(x-a)^n = A·(x-a)^(1-n)/(1-n)  [n≠1]")
        return "\n".join(sharh)

    @staticmethod
    def ta8yir_trigonometrique(naw3):
        """
        Trig Substitution patterns:
        √(a²-x²) → x = a·sin(θ)
        √(a²+x²) → x = a·tan(θ)
        √(x²-a²) → x = a·sec(θ)
        """
        sharh = []
        sharh.append(f"  ⚙️ Ta8yir Trigonométrique")
        
        if naw3 == "a2-x2":
            sharh.append(f"     √(a²-x²): Nkhtar x = a·sin(θ)")
            sharh.append(f"     dx = a·cos(θ)dθ")
            sharh.append(f"     √(a²-x²) = a·cos(θ)")
        elif naw3 == "a2+x2":
            sharh.append(f"     √(a²+x²): Nkhtar x = a·tan(θ)")
            sharh.append(f"     dx = a·sec²(θ)dθ")
            sharh.append(f"     √(a²+x²) = a·sec(θ)")
        elif naw3 == "x2-a2":
            sharh.append(f"     √(x²-a²): Nkhtar x = a·sec(θ)")
            sharh.append(f"     dx = a·sec(θ)tan(θ)dθ")
            sharh.append(f"     √(x²-a²) = a·tan(θ)")
        return "\n".join(sharh)

    @staticmethod
    def weierstrass(mo3adala):
        """
        Weierstrass Substitution: t = tan(x/2)
        
        Then:
        sin(x) = 2t/(1+t²)
        cos(x) = (1-t²)/(1+t²)
        dx = 2/(1+t²) dt
        
        Très utile pour ∫ R(sin(x), cos(x)) dx
        """
        sharh = []
        sharh.append(f"  ⚙️ Ta8yir Weierstrass (t = tan(x/2))")
        sharh.append(f"     Mo3adala: ∫ {mo3adala} dx")
        sharh.append(f"     Nkhtar: t = tan(x/2)")
        sharh.append(f"     sin(x) = 2t/(1+t²)")
        sharh.append(f"     cos(x) = (1-t²)/(1+t²)")
        sharh.append(f"     dx = 2/(1+t²) dt")
        sharh.append(f"     Nbeddel kol chi b t, o nhel integral rasyonnel")
        return "\n".join(sharh)

    @staticmethod
    def formule_reduction_sin(n):
        """
        Reduction formula for ∫sin^n(x)dx:
        ∫sin^n(x)dx = -sin^(n-1)(x)·cos(x)/n + (n-1)/n · ∫sin^(n-2)(x)dx
        """
        sharh = []
        sharh.append(f"  ⚙️ Formule de Réduction: ∫sin^{n}(x)dx")
        sharh.append(f"     = -sin^{n-1}(x)·cos(x)/{n} + {n-1}/{n} · ∫sin^{n-2}(x)dx")
        if n == 2:
            sharh.append(f"     ∫sin²(x)dx = x/2 - sin(2x)/4 + C")
        elif n == 3:
            sharh.append(f"     ∫sin³(x)dx = -cos(x) + cos³(x)/3 + C")
        elif n == 4:
            sharh.append(f"     ∫sin⁴(x)dx = 3x/8 - sin(2x)/4 + sin(4x)/32 + C")
        return "\n".join(sharh)

    @staticmethod
    def formule_reduction_cos(n):
        """
        Reduction formula for ∫cos^n(x)dx:
        ∫cos^n(x)dx = cos^(n-1)(x)·sin(x)/n + (n-1)/n · ∫cos^(n-2)(x)dx
        """
        sharh = []
        sharh.append(f"  ⚙️ Formule de Réduction: ∫cos^{n}(x)dx")
        sharh.append(f"     = cos^{n-1}(x)·sin(x)/{n} + {n-1}/{n} · ∫cos^{n-2}(x)dx")
        if n == 2:
            sharh.append(f"     ∫cos²(x)dx = x/2 + sin(2x)/4 + C")
        elif n == 3:
            sharh.append(f"     ∫cos³(x)dx = sin(x) - sin³(x)/3 + C")
        elif n == 4:
            sharh.append(f"     ∫cos⁴(x)dx = 3x/8 + sin(2x)/4 + sin(4x)/32 + C")
        return "\n".join(sharh)

    @staticmethod
    def formule_reduction_tan(n):
        """
        Reduction formula for ∫tan^n(x)dx:
        ∫tan^n(x)dx = tan^(n-1)(x)/(n-1) - ∫tan^(n-2)(x)dx
        """
        sharh = []
        sharh.append(f"  ⚙️ Formule de Réduction: ∫tan^{n}(x)dx")
        sharh.append(f"     = tan^{n-1}(x)/{n-1} - ∫tan^{n-2}(x)dx")
        return "\n".join(sharh)

    @staticmethod
    def formule_reduction_x_n_exp(n):
        """
        Reduction formula for ∫x^n·e^x dx:
        ∫x^n·e^x dx = x^n·e^x - n·∫x^(n-1)·e^x dx
        """
        sharh = []
        sharh.append(f"  ⚙️ Formule de Réduction: ∫x^{n}·e^x dx")
        sharh.append(f"     = x^{n}·e^x - {n}·∫x^{n-1}·e^x dx")
        if n == 1:
            sharh.append(f"     ∫x·e^x dx = x·e^x - e^x + C = (x-1)·e^x + C")
        elif n == 2:
            sharh.append(f"     ∫x²·e^x dx = x²·e^x - 2x·e^x + 2e^x + C = (x²-2x+2)·e^x + C")
        return "\n".join(sharh)

    @staticmethod
    def formule_reduction_ln_n(n):
        """
        Reduction formula for ∫(ln(x))^n dx:
        ∫(ln(x))^n dx = x·(ln(x))^n - n·∫(ln(x))^(n-1) dx
        """
        sharh = []
        sharh.append(f"  ⚙️ Formule de Réduction: ∫(ln(x))^{n} dx")
        sharh.append(f"     = x·(ln(x))^{n} - {n}·∫(ln(x))^{n-1} dx")
        if n == 1:
            sharh.append(f"     ∫ln(x)dx = x·ln(x) - x + C")
        elif n == 2:
            sharh.append(f"     ∫(ln(x))²dx = x·(ln(x))² - 2x·ln(x) + 2x + C")
        return "\n".join(sharh)

    @staticmethod
    def takamol_feynman_sharh():
        """
        Feynman's Technique: Differentiation Under the Integral Sign
        (Leibniz integral rule)
        
        d/da ∫f(x,a)dx = ∫ ∂f/∂a dx
        
        Famous example: ∫₀^∞ sin(x)/x dx = π/2
        By introducing: I(a) = ∫₀^∞ e^(-ax)·sin(x)/x dx
        """
        sharh = []
        sharh.append(f"  ⚙️ Tari9at Feynman (Differentiation Under Integral)")
        sharh.append(f"     Qa3ida: d/da ∫f(x,a)dx = ∫ ∂f/∂a dx")
        sharh.append(f"     ")
        sharh.append(f"     Mithal mashur:")
        sharh.append(f"     ∫₀^∞ sin(x)/x dx:")
        sharh.append(f"     1. Ndakhlu parameter: I(a) = ∫₀^∞ e^(-ax)·sin(x)/x dx")
        sharh.append(f"     2. I'(a) = -∫₀^∞ e^(-ax)·sin(x) dx = -1/(1+a²)")
        sharh.append(f"     3. I(a) = -arctan(a) + C")
        sharh.append(f"     4. I(∞) = 0 => C = π/2")
        sharh.append(f"     5. I(0) = π/2  ✓")
        return "\n".join(sharh)

    @staticmethod
    def takamol_b_dl(mo3adala, bidaya, nihaya, daraja=15):
        """
        Integration via Taylor Series (DL):
        If f(x) has no elementary antiderivative, expand as DL
        and integrate term by term.
        
        Examples:
        - ∫e^(-x²)dx (Gaussian integral)
        - ∫sin(x)/x dx (Sine integral)
        - ∫cos(x)/x dx (Cosine integral)
        """
        sharh = []
        sharh.append(f"  ⚙️ Takamol b-DL (Integration via Taylor Series)")
        sharh.append(f"     Mo3adala: ∫ {mo3adala} dx from {bidaya} to {nihaya}")
        sharh.append(f"     Methodology: Expand into DL, then integrate term-by-term")
        
        # Try to detect which DL to use
        m = mo3adala.replace(" ", "")
        
        if "e^(-x^2)" in m or "e^(-x**2)" in m or "exp(-x^2)" in m:
            sharh.append(f"     Detected: Gaussian function e^(-x²)")
            sharh.append(f"     e^(-x²) = 1 - x² + x⁴/2! - x⁶/3! + ...")
            sharh.append(f"     ∫e^(-x²)dx = x - x³/3 + x⁵/(5·2!) - x⁷/(7·3!) + ...")
            
            natija = 0.0
            for n in range(daraja + 1):
                qowa = 2 * n + 1
                ishara = (-1) ** n
                mu3amil = ishara / (math.factorial(n) * qowa)
                natija += mu3amil * (nihaya ** qowa) - mu3amil * (bidaya ** qowa)
            sharh.append(f"     Natija (DL, {daraja} terms): {natija:.10f}")
            return "\n".join(sharh), natija
        
        elif "sin(x)/x" in m or "sinc" in m:
            sharh.append(f"     Detected: Sine Integral Si(x) = ∫sin(x)/x dx")
            sharh.append(f"     sin(x)/x = 1 - x²/3! + x⁴/5! - ...")
            sharh.append(f"     ∫sin(x)/x dx = x - x³/(3·3!) + x⁵/(5·5!) - ...")
            
            natija = 0.0
            for n in range(daraja + 1):
                qowa = 2 * n + 1
                ishara = (-1) ** n
                mu3amil = ishara / (math.factorial(qowa) * qowa)
                natija += mu3amil * (nihaya ** qowa) - mu3amil * (bidaya ** qowa)
            sharh.append(f"     Natija (DL, {daraja} terms): {natija:.10f}")
            return "\n".join(sharh), natija
        
        else:
            sharh.append(f"     Malkitsh DL me3ruf, ghadi nesta3mel hel_adadi...")
            return "\n".join(sharh), None


# ═══════════════════════════════════════════════════════════════
#  SECTION 2: HELPER FUNCTIONS (Parsing & Utilities)
# ═══════════════════════════════════════════════════════════════

def naqqi_mo3adala(mo3adala: str) -> str:
    """
    Preprocessing / Smart Simplification
    naqqi = clean | mo3adala = equation
    """
    natija = mo3adala.strip()
    
    # Remove all spaces
    natija = natija.replace(" ", "")
    
    # --- FIX: Remove trailing 'dx' or 'dt' if user types it ---
    if natija.lower().endswith("dx"):
        natija = natija[:-2]
    elif natija.lower().endswith("dt"):
        natija = natija[:-2]
        
    # Remove ^1 (redundant power)
    natija = natija.replace("^1", "")
    
    # --- Trig Identity: sin²(x) + cos²(x) = 1 ---
    trig_patterns = [
        ("sin(x)^2+cos(x)^2", "1"),
        ("cos(x)^2+sin(x)^2", "1"),
        ("sin(x)**2+cos(x)**2", "1"),
        ("cos(x)**2+sin(x)**2", "1"),
        ("sin^2(x)+cos^2(x)", "1"),
        ("cos^2(x)+sin^2(x)", "1"),
        # Handle cases with arguments like (x+1)
        # Note: This simple replace works for exact string matches.
        # For (x+1), the code relies on normal integration rules.
    ]
    for qadim, jadid in trig_patterns:
        natija = natija.replace(qadim, jadid)
    
    # Normalize ** to ^ for internal processing
    natija = natija.replace("**", "^")
    
    return natija


def lqa_aqwas_muwaziya(silsila: str, mawqi3: int) -> int:
    """
    Find matching closing parenthesis.
    lqa = find | aqwas = parentheses | muwaziya = matching
    mawqi3 = position
    """
    omq = 0  # depth - but can't start var with digit in Python
    for i in range(mawqi3, len(silsila)):
        if silsila[i] == '(':
            omq += 1
        elif silsila[i] == ')':
            omq -= 1
            if omq == 0:
                return i
    return -1


def qassem_3ala_3amil(silsila: str, ramz: str) -> List[str]:
    """
    Split string on operator, respecting parentheses depth.
    qassem = split | 3amil = operator | ramz = symbol
    
    Returns list of parts split at top-level occurrences of ramz.
    """
    ajza2 = []  # parts
    omq = 0  # depth
    bidaya_hadd = 0  # start of current term
    
    i = 0
    while i < len(silsila):
        harf = silsila[i]
        if harf == '(':
            omq += 1
        elif harf == ')':
            omq -= 1
        elif omq == 0:
            if ramz == '+' and harf == '+':
                ajza2.append(silsila[bidaya_hadd:i])
                bidaya_hadd = i + 1
            elif ramz == '-' and harf == '-' and i > 0:
                # Make sure it's not a negative sign at start or after operator
                harf_qabl = silsila[i - 1] if i > 0 else ''
                if harf_qabl not in ('', '+', '-', '*', '/', '^', '('):
                    ajza2.append(silsila[bidaya_hadd:i])
                    bidaya_hadd = i  # keep the minus sign with next term
        i += 1
    
    ajza2.append(silsila[bidaya_hadd:])
    
    # Filter out empty strings
    ajza2 = [j for j in ajza2 if j.strip()]
    
    return ajza2


def qassem_jam3_tar7(silsila: str) -> List[str]:
    """
    Split on + and - at top level (outside parentheses), preserving signs.
    jam3 = addition | tar7 = subtraction
    """
    hudud = []  # terms
    omq = 0
    hadd_hali = ""  # current term
    
    for i, harf in enumerate(silsila):
        if harf == '(':
            omq += 1
            hadd_hali += harf
        elif harf == ')':
            omq -= 1
            hadd_hali += harf
        elif omq == 0 and harf in ('+', '-') and i > 0:
            # Check it's not part of exponent like e^-2
            harf_qabl = silsila[i - 1] if i > 0 else ''
            if harf_qabl == '^':
                hadd_hali += harf
            else:
                if hadd_hali.strip():
                    hudud.append(hadd_hali.strip())
                hadd_hali = harf if harf == '-' else ""
        else:
            hadd_hali += harf
    
    if hadd_hali.strip():
        hudud.append(hadd_hali.strip())
    
    return hudud


def stakhrej_mu3amil(hadd: str) -> Tuple[Optional[float], Optional[str]]:
    """
    Extract constant multiplier from term.
    stakhrej = extract | mu3amil = coefficient
    
    Examples:
        "5*sin(x)" -> (5.0, "sin(x)")
        "-3*x^2" -> (-3.0, "x^2")
        "sin(x)" -> (1.0, "sin(x)")
        "7" -> (7.0, None)  -- pure constant
        "-x" -> (-1.0, "x")
    """
    hadd = hadd.strip()
    
    if not hadd:
        return None, None
    
    # Check for leading negative
    ishara = 1.0
    if hadd.startswith('-'):
        ishara = -1.0
        hadd = hadd[1:]
    elif hadd.startswith('+'):
        hadd = hadd[1:]
    
    # Look for pattern: number * rest
    match_darb = re.match(r'^([\d.]+)\*(.+)$', hadd)
    if match_darb:
        raqm = float(match_darb.group(1)) * ishara
        baqiya = match_darb.group(2)
        return raqm, baqiya
    
    # Check if it's purely a number
    try:
        raqm = float(hadd) * ishara
        return raqm, None
    except ValueError:
        pass
    
    # It's a function with implicit coefficient 1
    return ishara, hadd


def stakhrej_dakhil_dalat(silsila: str, ism_dalla: str) -> Optional[str]:
    """
    Extract the argument inside a function call.
    stakhrej = extract | dakhil = inside | dalla = function
    
    Example: stakhrej_dakhil_dalat("sin(2*x+3)", "sin") -> "2*x+3"
    """
    idx = silsila.find(ism_dalla + "(")
    if idx == -1:
        return None
    
    bidaya_qaws = idx + len(ism_dalla)
    nihaya_qaws = lqa_aqwas_muwaziya(silsila, bidaya_qaws)
    
    if nihaya_qaws == -1:
        return None
    
    dakhil = silsila[bidaya_qaws + 1:nihaya_qaws]
    
    # Check that the function name is exactly at the start or after operator
    if idx > 0 and silsila[idx - 1].isalpha():
        return None  # e.g., "asin" when looking for "sin"
    
    return dakhil


def hallel_khatiyya(dakhil: str) -> Tuple[Optional[float], Optional[float]]:
    """
    Parse linear expression ax+b.
    hallel = parse | khatiyya = linear
    
    Returns (a, b) where dakhil = a*x + b
    Examples:
        "2*x+3" -> (2.0, 3.0)
        "x" -> (1.0, 0.0)
        "-x+5" -> (-1.0, 5.0)
        "3*x" -> (3.0, 0.0)
        "x-1" -> (1.0, -1.0)
    """
    dakhil = dakhil.strip()
    
    if dakhil == 'x':
        return 1.0, 0.0
    if dakhil == '-x':
        return -1.0, 0.0
    
    # Try pattern: a*x+b or a*x-b
    match1 = re.match(r'^(-?[\d.]*)\*?x([+-][\d.]+)?$', dakhil)
    if match1:
        a_str = match1.group(1)
        b_str = match1.group(2)
        
        if a_str in ('', '+'):
            a = 1.0
        elif a_str == '-':
            a = -1.0
        else:
            a = float(a_str)
        
        b = float(b_str) if b_str else 0.0
        return a, b
    
    # Try pattern: x*a+b
    match2 = re.match(r'^x\*(-?[\d.]+)([+-][\d.]+)?$', dakhil)
    if match2:
        a = float(match2.group(1))
        b_str = match2.group(2)
        b = float(b_str) if b_str else 0.0
        return a, b
    
    # Simple x+b or x-b
    match3 = re.match(r'^x([+-][\d.]+)$', dakhil)
    if match3:
        return 1.0, float(match3.group(1))
    
    return None, None


# ═══════════════════════════════════════════════════════════════
#  SECTION 3: THE SYMBOLIC SOLVER (hel_ramzi)
# ═══════════════════════════════════════════════════════════════

def hel_ramzi(mo3adala: str, omq_max: int = 10) -> Optional[str]:
    """
    THE MAIN SYMBOLIC INTEGRAL SOLVER
    Added Depth Limit to prevent Infinite Recursion
    """
    # Safety Brake
    if omq_max <= 0:
        return None
        
    mo3adala = naqqi_mo3adala(mo3adala)
    
    if not mo3adala:
        return None
    
    # ─── Fix for sin^2(u) + cos^2(u) = 1 (General Case) ───
    # Check if we have sin^2(...) + cos^2(...) with SAME content
    # This is a smart check using Regex
    pattern_trig = re.search(r'sin\^2\((.+?)\)\+cos\^2\((.+?)\)', mo3adala.replace(" ", ""))
    if pattern_trig:
        u1 = pattern_trig.group(1)
        u2 = pattern_trig.group(2)
        if u1 == u2:
            # It is exactly sin^2(u) + cos^2(u)
            # Replace the whole match with "1"
            mo3adala = mo3adala.replace(pattern_trig.group(0), "1")
            
    # Also check the reverse order: cos^2 + sin^2
    pattern_trig2 = re.search(r'cos\^2\((.+?)\)\+sin\^2\((.+?)\)', mo3adala.replace(" ", ""))
    if pattern_trig2:
        u1 = pattern_trig2.group(1)
        u2 = pattern_trig2.group(2)
        if u1 == u2:
            mo3adala = mo3adala.replace(pattern_trig2.group(0), "1")

    # ─── STEP 2: Recursive Splitting (Linearity) ───
    hudud = qassem_jam3_tar7(mo3adala)
    
    if len(hudud) > 1:
        natija_ajza2 = []
        for hadd in hudud:
            # Decrease depth for recursive calls
            natija_hadd = hel_ramzi(hadd, omq_max - 1)
            if natija_hadd is None:
                return None
            natija_ajza2.append(natija_hadd)
        
        # Join with proper signs
        natija_kamilat = natija_ajza2[0]
        for i in range(1, len(natija_ajza2)):
            j = natija_ajza2[i].strip()
            if j.startswith('-'):
                natija_kamilat += " " + j
            else:
                natija_kamilat += " + " + j
        return natija_kamilat
    
    # ─── STEP 3: Constant Multiplier Extraction ───
    mu3amil, baqiya = stakhrej_mu3amil(mo3adala)
    
    if mu3amil is not None and baqiya is not None:
        # Check to avoid infinite loop: if baqiya is same as mo3adala (e.g. "sin(x)" -> 1 * "sin(x)")
        if baqiya == mo3adala:
            # Skip extraction if it didn't simplify anything
            pass
        else:
            natija_baqiya = hel_ramzi(baqiya, omq_max - 1)
            if natija_baqiya is not None:
                if mu3amil == 1.0:
                    return natija_baqiya
                elif mu3amil == -1.0:
                    return f"-({natija_baqiya})"
                else:
                    if mu3amil == int(mu3amil):
                        mu3amil_str = str(int(mu3amil))
                    else:
                        mu3amil_str = f"{mu3amil:.6g}"
                    return f"{mu3amil_str}*({natija_baqiya})"
    
    if baqiya is None and mu3amil is not None:
        # Pure constant
        if mu3amil == int(mu3amil):
            return f"{int(mu3amil)}*x"
        return f"{mu3amil:.6g}*x"
    
    m = mo3adala
    
    # ─── STEP 4, 5, 6 ───
    natija = _jarreb_qa3ida_mubashira(m)
    if natija is not None: return natija
    
    natija = _jarreb_tarkib_khatiy(m)
    if natija is not None: return natija
    
    natija = _jarreb_qawa3id_mutaqaddima(m)
    if natija is not None: return natija
    
    return None


def _jarreb_qa3ida_mubashira(m: str) -> Optional[str]:
    """
    Try direct/exact integration rules.
    UPDATED: Now handles constants in numerator (e.g., 4/(1+x^2))
    """
    
    # ════════════════════════
    # CONSTANT & POWER RULES
    # ════════════════════════
    try:
        raqm = float(m)
        if raqm == int(raqm): return f"{int(raqm)}*x"
        return f"{raqm}*x"
    except ValueError: pass
    
    if m == 'x': return "x^2/2"
    
    # Power Rule x^n
    match_power = re.match(r'^x\^(-?[\d.]+(?:/[\d.]+)?)$', m)
    if match_power:
        n_str = match_power.group(1)
        try:
            if '/' in n_str:
                n_val = float(n_str.split('/')[0])/float(n_str.split('/')[1])
            else:
                n_val = float(n_str)
                
            if n_val == -1: return "log(|x|)"
            new_pow = n_val + 1
            # Format nicely
            mu3amil = 1.0/new_pow
            pow_str = f"{new_pow:.4g}" if new_pow != int(new_pow) else str(int(new_pow))
            mu3_str = f"{mu3amil:.4g}" if mu3amil != int(mu3amil) else (str(int(mu3amil)) if mu3amil!=1 else "")
            
            if mu3_str: return f"{mu3_str}*x^{pow_str}"
            return f"x^{pow_str}"
        except: pass

    # ════════════════════════════════
    # INVERSE & LOG RULES (Generalized A/x)
    # ════════════════════════════════
    # Match A/x
    match_inv = re.match(r'^([\d.]+)/x$', m)
    if match_inv:
        a = match_inv.group(1)
        return f"{a}*log(|x|)"
    if m in ('1/x', 'x^-1'): return "log(|x|)"

    # ════════════════════════════════
    # EXPONENTIAL
    # ════════════════════════════════
    if m in ('exp(x)', 'e^x'): return "e^x"
    # Match A*exp(x) or similar handled by extraction logic usually, 
    # but let's handle A^x
    match_ax = re.match(r'^([\d.]+)\^x$', m)
    if match_ax:
        a = float(match_ax.group(1))
        if a > 0 and a!=1: return f"{a}^x/log({a})"

    # ════════════════════════════════
    # TRIGONOMETRIC (Generalized)
    # ════════════════════════════════
    if m == 'sin(x)': return "-cos(x)"
    if m == 'cos(x)': return "sin(x)"
    if m == 'tan(x)': return "-log(|cos(x)|)"
    if m in ('sec(x)^2', '1/cos(x)^2'): return "tan(x)"
    if m in ('csc(x)^2', '1/sin(x)^2'): return "-cot(x)"
    
    # ════════════════════════════════
    # INVERSE TRIG (The fix for 4/(1+x^2))
    # ════════════════════════════════
    
    # Pattern: A / (1 + x^2) -> A * arctan(x)
    match_atan = re.match(r'^([\d.]+)/\(1\+x\^2\)$', m)
    if match_atan:
        a = match_atan.group(1)
        if float(a) == 1.0: return "arctan(x)"
        return f"{a}*arctan(x)"
    if m == '1/(1+x^2)': return "arctan(x)"

    # Pattern: A / sqrt(1 - x^2) -> A * arcsin(x)
    match_asin = re.match(r'^([\d.]+)/sqrt\(1-x\^2\)$', m)
    if match_asin:
        a = match_asin.group(1)
        if float(a) == 1.0: return "arcsin(x)"
        return f"{a}*arcsin(x)"
    if m in ('1/sqrt(1-x^2)',): return "arcsin(x)"
    
    # ════════════════════════════════
    # SQRT RULES (Generalized)
    # ════════════════════════════════
    # Pattern: A / sqrt(x) -> 2*A*sqrt(x)
    match_sqrt_inv = re.match(r'^([\d.]+)/sqrt\(x\)$', m)
    if match_sqrt_inv:
        a = float(match_sqrt_inv.group(1))
        return f"{2*a:.4g}*sqrt(x)"
    if m == '1/sqrt(x)': return "2*sqrt(x)"
    
    if m == 'sqrt(x)': return "(2/3)*x^(3/2)"

    # ════════════════════════════════
    # SPECIAL FRACTIONS
    # ════════════════════════════════
    # A / (x^2 + 1) is same as A / (1 + x^2)
    match_atan_2 = re.match(r'^([\d.]+)/\(x\^2\+1\)$', m)
    if match_atan_2:
        a = match_atan_2.group(1)
        return f"{a}*arctan(x)"
    if m in ('1/(x^2+1)',): return "arctan(x)"
    
    # ════════════════════════════════
    # OTHER TRIG
    # ════════════════════════════════
    if m in ('cot(x)', 'cotan(x)'): return "log(|sin(x)|)"
    if m in ('sec(x)', '1/cos(x)'): return "log(|sec(x)+tan(x)|)"
    if m in ('csc(x)', 'cosec(x)', '1/sin(x)'): return "-log(|csc(x)+cot(x)|)"
    if m in ('sec(x)*tan(x)', 'tan(x)*sec(x)'): return "sec(x)"
    if m in ('csc(x)*cot(x)', 'cot(x)*csc(x)'): return "-csc(x)"
    
    # ════════════════════════════════
    # INVERSE TRIG (continued)
    # ════════════════════════════════
    if m in ('-1/sqrt(1-x^2)',): return "-arcsin(x)"
    if m in ('arctan(x)', 'atan(x)'): return "x*arctan(x) - log(1+x^2)/2"
    if m in ('arcsin(x)', 'asin(x)'): return "x*arcsin(x) + sqrt(1-x^2)"
    if m in ('arccos(x)', 'acos(x)'): return "x*arccos(x) - sqrt(1-x^2)"
    
    # ════════════════════════════════
    # LOGARITHMIC
    # ════════════════════════════════
    if m in ('log(x)', 'ln(x)'): return "x*log(x) - x"
    if m in ('log(x)^2', 'ln(x)^2', '(log(x))^2', '(ln(x))^2'): return "x*(log(x))^2 - 2*x*log(x) + 2*x"
    if m in ('1/(x*log(x))', '1/(x*ln(x))'): return "log(log(x))"
    
    # ════════════════════════════════
    # HYPERBOLIC
    # ════════════════════════════════
    if m == 'sinh(x)': return "cosh(x)"
    if m == 'cosh(x)': return "sinh(x)"
    if m == 'tanh(x)': return "log(cosh(x))"
    if m == 'coth(x)': return "log(|sinh(x)|)"
    if m in ('sech(x)^2', 'sech^2(x)'): return "tanh(x)"
    if m in ('csch(x)^2', 'csch^2(x)'): return "-coth(x)"
    
    # ════════════════════════════════
    # INVERSE HYPERBOLIC
    # ════════════════════════════════
    if m in ('1/sqrt(x^2+1)', '1/(x^2+1)^(1/2)'): return "arcsinh(x)"
    if m in ('1/sqrt(x^2-1)', '1/(x^2-1)^(1/2)'): return "arccosh(x)"
    
    # ════════════════════════════════
    # SPECIAL FORMS with 1/(ax²+bx+c)
    # ════════════════════════════════
    # ∫1/(x²+a²) = (1/a)*arctan(x/a)
    match_x2a2 = re.match(r'^1/\(x\^2\+([\d.]+)\)$', m)
    if match_x2a2:
        a2 = float(match_x2a2.group(1))
        a = math.sqrt(a2)
        return f"(1/{a:.6g})*arctan(x/{a:.6g})"
    
    # ∫1/(a²+x²) same thing
    match_a2x2 = re.match(r'^1/\(([\d.]+)\+x\^2\)$', m)
    if match_a2x2:
        a2 = float(match_a2x2.group(1))
        a = math.sqrt(a2)
        return f"(1/{a:.6g})*arctan(x/{a:.6g})"
    
    # ∫1/(x²-a²) = (1/(2a))*ln|(x-a)/(x+a)|
    match_x2_minus_a2 = re.match(r'^1/\(x\^2-([\d.]+)\)$', m)
    if match_x2_minus_a2:
        a2 = float(match_x2_minus_a2.group(1))
        a = math.sqrt(a2)
        return f"(1/{2*a:.6g})*log(|(x-{a:.6g})/(x+{a:.6g})|)"
    
    # ∫x/(x²+1) = ln(x²+1)/2
    if m in ('x/(x^2+1)', 'x/(1+x^2)'): return "log(x^2+1)/2"
    
    # ∫x/(x²+a²) = ln(x²+a²)/2
    match_x_over_x2a2 = re.match(r'^x/\(x\^2\+([\d.]+)\)$', m)
    if match_x_over_x2a2:
        a2 = float(match_x_over_x2a2.group(1))
        return f"log(x^2+{a2})/2"
    
    # ════════════════════════════════
    # TRIG POWERS (sin^n, cos^n)
    # ════════════════════════════════
    if m in ('sin(x)^2', 'sin^2(x)', '(sin(x))^2'): return "x/2 - sin(2*x)/4"
    if m in ('cos(x)^2', 'cos^2(x)', '(cos(x))^2'): return "x/2 + sin(2*x)/4"
    if m in ('sin(x)^3', 'sin^3(x)', '(sin(x))^3'): return "-cos(x) + (cos(x))^3/3"
    if m in ('cos(x)^3', 'cos^3(x)', '(cos(x))^3'): return "sin(x) - (sin(x))^3/3"
    if m in ('sin(x)^4', 'sin^4(x)', '(sin(x))^4'): return "3*x/8 - sin(2*x)/4 + sin(4*x)/32"
    if m in ('cos(x)^4', 'cos^4(x)', '(cos(x))^4'): return "3*x/8 + sin(2*x)/4 + sin(4*x)/32"
    if m in ('tan(x)^2', 'tan^2(x)', '(tan(x))^2'): return "tan(x) - x"
    if m in ('cot(x)^2', 'cot^2(x)', '(cot(x))^2'): return "-cot(x) - x"
    
    # ════════════════════════════════
    # PRODUCTS: sin*cos, x*exp, x*ln, etc.
    # ════════════════════════════════
    if m in ('sin(x)*cos(x)', 'cos(x)*sin(x)'): return "(sin(x))^2/2"
    if m in ('x*exp(x)', 'x*e^x', 'exp(x)*x', 'e^x*x'): return "(x-1)*e^x"
    if m in ('x^2*exp(x)', 'x^2*e^x'): return "(x^2-2*x+2)*e^x"
    if m in ('x*sin(x)', 'sin(x)*x'): return "sin(x) - x*cos(x)"
    if m in ('x*cos(x)', 'cos(x)*x'): return "cos(x) + x*sin(x)"
    if m in ('x*log(x)', 'x*ln(x)', 'log(x)*x', 'ln(x)*x'): return "x^2*log(x)/2 - x^2/4"
    if m in ('x^2*log(x)', 'x^2*ln(x)'): return "x^3*log(x)/3 - x^3/9"
    if m in ('log(x)/x', 'ln(x)/x'): return "(log(x))^2/2"
    if m in ('exp(x)*sin(x)', 'e^x*sin(x)', 'sin(x)*exp(x)', 'sin(x)*e^x'): return "e^x*(sin(x)-cos(x))/2"
    if m in ('exp(x)*cos(x)', 'e^x*cos(x)', 'cos(x)*exp(x)', 'cos(x)*e^x'): return "e^x*(sin(x)+cos(x))/2"
    
    # ════════════════════════════════
    # SPECIAL INTEGRALS
    # ════════════════════════════════
    if m in ('sqrt(1-x^2)', '(1-x^2)^(1/2)'): return "(x*sqrt(1-x^2) + arcsin(x))/2"
    if m in ('sqrt(x^2+1)', '(x^2+1)^(1/2)', 'sqrt(1+x^2)'): return "(x*sqrt(x^2+1) + log(x+sqrt(x^2+1)))/2"
    if m in ('sqrt(x^2-1)', '(x^2-1)^(1/2)'): return "(x*sqrt(x^2-1) - log(|x+sqrt(x^2-1)|))/2"
    if m in ('1/(x*sqrt(x^2-1))',): return "arccos(1/x)"
    if m in ('x*sqrt(x^2+1)',): return "(x^2+1)^(3/2)/3"
    if m in ('abs(x)', '|x|'): return "x*|x|/2"
    if m in ('1/(1+e^x)', '1/(1+exp(x))'): return "x - log(1+e^x)"
    if m == '1/(x^2+x+1)': return "(2/sqrt(3))*arctan((2*x+1)/sqrt(3))"
    if m in ('log(1+x)', 'ln(1+x)', 'log(x+1)', 'ln(x+1)'): return "(1+x)*log(1+x) - x"
    
    # ∫log(a+x) for general a
    match_log_apx = re.match(r'^(?:log|ln)\(([\d.]+)\+x\)$', m)
    if match_log_apx:
        a = match_log_apx.group(1)
        return f"({a}+x)*log({a}+x) - x"
    
    match_log_xpa = re.match(r'^(?:log|ln)\(x\+([\d.]+)\)$', m)
    if match_log_xpa:
        a = match_log_xpa.group(1)
        return f"(x+{a})*log(x+{a}) - x"
    
    # ∫1/(x+a) = log|x+a|
    match_1_xpa = re.match(r'^1/\(x\+([+-]?[\d.]+)\)$', m)
    if match_1_xpa:
        a = match_1_xpa.group(1)
        return f"log(|x+{a}|)"
    
    match_1_apx = re.match(r'^1/\(([+-]?[\d.]+)\+x\)$', m)
    if match_1_apx:
        a = match_1_apx.group(1)
        return f"log(|{a}+x|)"
    
    # ∫x^n * e^(-x) patterns
    if m in ('x*e^(-x)', 'x*exp(-x)'): return "-(x+1)*e^(-x)"
    if m in ('x^2*e^(-x)', 'x^2*exp(-x)'): return "-(x^2+2*x+2)*e^(-x)"
    
    return None


def _jarreb_tarkib_khatiy(m: str) -> Optional[str]:
    """
    Try Linear Composition Rule (Chain Rule Reverse):
    If f(ax+b), divide the antiderivative by a.
    
    jarreb = try | tarkib = composition | khatiy = linear
    """
    
    # List of functions and their integrals
    # (function_name, integral_of_f(x), needs_negative)
    qawa3id_dalat = [
        ('sin', '-cos', False),
        ('cos', 'sin', False),
        ('tan', '-log(|cos|)', False),
        ('cot', 'log(|sin|)', False),
        ('exp', 'exp', False),
        ('sec', 'log(|sec+tan|)', False),  # simplified
        ('csc', '-log(|csc+cot|)', False),
        ('sinh', 'cosh', False),
        ('cosh', 'sinh', False),
        ('tanh', 'log(cosh)', False),
    ]
    
    for ism_dalla, natija_asasiya, _ in qawa3id_dalat:
        dakhil = stakhrej_dakhil_dalat(m, ism_dalla)
        if dakhil is None:
            continue
        
        # Check if the entire string is just this function call
        expected = f"{ism_dalla}({dakhil})"
        # Also handle potential ^2 etc after
        if m != expected:
            # Check with power: sin(ax+b)^2 etc - skip, handled elsewhere
            continue
        
        a, b = hallel_khatiyya(dakhil)
        if a is None:
            continue
        
        # Build the result
        if a == 1.0 and b == 0.0:
            # Already handled in direct rules
            continue
        
        dakhil_str = dakhil
        
        if ism_dalla == 'sin':
            natija = f"(-1/{a:.6g})*cos({dakhil_str})"
        elif ism_dalla == 'cos':
            natija = f"(1/{a:.6g})*sin({dakhil_str})"
        elif ism_dalla == 'tan':
            natija = f"(-1/{a:.6g})*log(|cos({dakhil_str})|)"
        elif ism_dalla == 'cot':
            natija = f"(1/{a:.6g})*log(|sin({dakhil_str})|)"
        elif ism_dalla == 'exp':
            natija = f"(1/{a:.6g})*exp({dakhil_str})"
        elif ism_dalla == 'sinh':
            natija = f"(1/{a:.6g})*cosh({dakhil_str})"
        elif ism_dalla == 'cosh':
            natija = f"(1/{a:.6g})*sinh({dakhil_str})"
        elif ism_dalla == 'tanh':
            natija = f"(1/{a:.6g})*log(cosh({dakhil_str}))"
        elif ism_dalla == 'sec':
            natija = f"(1/{a:.6g})*log(|sec({dakhil_str})+tan({dakhil_str})|)"
        elif ism_dalla == 'csc':
            natija = f"(-1/{a:.6g})*log(|csc({dakhil_str})+cot({dakhil_str})|)"
        else:
            continue
        
        # Simplify if a = 1
        if a == 1.0:
            continue  # Already handled above
        
        return natija
    
    # ─── e^(ax+b) ───
    match_eax = re.match(r'^e\^\((.+)\)$', m)
    if match_eax:
        dakhil = match_eax.group(1)
        a, b = hallel_khatiyya(dakhil)
        if a is not None and (a != 1.0 or b != 0.0):
            return f"(1/{a:.6g})*e^({dakhil})"
    
    # ─── (ax+b)^n ───
    match_lin_power = re.match(r'^\((.+)\)\^(-?[\d.]+(?:/[\d.]+)?)$', m)
    if match_lin_power:
        dakhil = match_lin_power.group(1)
        n_str = match_lin_power.group(2)
        
        if '/' in n_str:
            parts = n_str.split('/')
            n_val = float(parts[0]) / float(parts[1])
        else:
            n_val = float(n_str)
        
        a, b = hallel_khatiyya(dakhil)
        if a is not None:
            if n_val == -1:
                return f"(1/{a:.6g})*log(|{dakhil}|)"
            new_power = n_val + 1
            mu3amil = 1.0 / (a * new_power)
            new_power_str = f"{new_power:.6g}" if new_power != int(new_power) else str(int(new_power))
            return f"{mu3amil:.6g}*({dakhil})^{new_power_str}"
    
    # ─── 1/(ax+b) ───
    match_1_lin = re.match(r'^1/\((.+)\)$', m)
    if match_1_lin:
        dakhil = match_1_lin.group(1)
        a, b = hallel_khatiyya(dakhil)
        if a is not None:
            return f"(1/{a:.6g})*log(|{dakhil}|)"
    
    # ─── sqrt(ax+b) ───
    match_sqrt_lin = re.match(r'^sqrt\((.+)\)$', m)
    if match_sqrt_lin:
        dakhil = match_sqrt_lin.group(1)
        a, b = hallel_khatiyya(dakhil)
        if a is not None:
            return f"(2/(3*{a:.6g}))*({dakhil})^(3/2)"
    
    return None


def _jarreb_qawa3id_mutaqaddima(m: str) -> Optional[str]:
    """
    Try advanced rules: trig power reduction, specific patterns.
    jarreb = try | qawa3id = rules | mutaqaddima = advanced
    """
    
    # ─── sin(ax) * cos(bx) ───
    match_sc = re.match(r'^sin\(([\d.]*)\*?x\)\*cos\(([\d.]*)\*?x\)$', m)
    if match_sc:
        a = float(match_sc.group(1)) if match_sc.group(1) else 1.0
        b_val = float(match_sc.group(2)) if match_sc.group(2) else 1.0
        if a == b_val:
            return f"-cos({2*a:.6g}*x)/(2*{2*a:.6g})"
        # Product-to-sum: sin(a)cos(b) = [sin(a+b) + sin(a-b)] / 2
        apb = a + b_val
        amb = a - b_val
        return f"-cos({apb:.6g}*x)/(2*{apb:.6g}) - cos({amb:.6g}*x)/(2*{amb:.6g})"
    
    # ─── sin(ax) * sin(bx) ───
    match_ss = re.match(r'^sin\(([\d.]*)\*?x\)\*sin\(([\d.]*)\*?x\)$', m)
    if match_ss:
        a = float(match_ss.group(1)) if match_ss.group(1) else 1.0
        b_val = float(match_ss.group(2)) if match_ss.group(2) else 1.0
        # sin(a)sin(b) = [cos(a-b) - cos(a+b)] / 2
        apb = a + b_val
        amb = a - b_val
        if amb == 0:
            return f"x/2 - sin({apb:.6g}*x)/(2*{apb:.6g})"
        return f"sin({amb:.6g}*x)/(2*{amb:.6g}) - sin({apb:.6g}*x)/(2*{apb:.6g})"
    
    # ─── cos(ax) * cos(bx) ───
    match_cc = re.match(r'^cos\(([\d.]*)\*?x\)\*cos\(([\d.]*)\*?x\)$', m)
    if match_cc:
        a = float(match_cc.group(1)) if match_cc.group(1) else 1.0
        b_val = float(match_cc.group(2)) if match_cc.group(2) else 1.0
        apb = a + b_val
        amb = a - b_val
        if amb == 0:
            return f"x/2 + sin({apb:.6g}*x)/(2*{apb:.6g})"
        return f"sin({amb:.6g}*x)/(2*{amb:.6g}) + sin({apb:.6g}*x)/(2*{apb:.6g})"
    
    # ─── sin(x)^n * cos(x)^m patterns ───
    # ∫sin(x)*cos(x)^n = -cos(x)^(n+1)/(n+1)
    match_sc_n = re.match(r'^sin\(x\)\*cos\(x\)\^([\d.]+)$', m)
    if match_sc_n:
        n_val = float(match_sc_n.group(1))
        new_p = n_val + 1
        return f"-cos(x)^{new_p:.6g}/{new_p:.6g}"
    
    # ∫cos(x)*sin(x)^n = sin(x)^(n+1)/(n+1)
    match_cs_n = re.match(r'^cos\(x\)\*sin\(x\)\^([\d.]+)$', m)
    if match_cs_n:
        n_val = float(match_cs_n.group(1))
        new_p = n_val + 1
        return f"sin(x)^{new_p:.6g}/{new_p:.6g}"
    
    # ─── Wallis-type integrals (will need numeric for most) ───
    
    # ─── Rational functions: try partial fraction heuristic ───
    # ∫1/(x²+bx+c) - complete the square
    match_quad_denom = re.match(r'^1/\(x\^2([+-][\d.]*)\*?x([+-][\d.]+)\)$', m)
    if match_quad_denom:
        try:
            b_str = match_quad_denom.group(1)
            c_str = match_quad_denom.group(2)
            b_coef = float(b_str.replace('*', ''))
            c_val = float(c_str)
            
            # x² + bx + c = (x + b/2)² + (c - b²/4)
            shift = b_coef / 2
            remainder = c_val - (b_coef ** 2) / 4
            
            if remainder > 0:
                a_sq = math.sqrt(remainder)
                return f"(1/{a_sq:.6g})*arctan((x+{shift:.6g})/{a_sq:.6g})"
            elif remainder < 0:
                a_sq = math.sqrt(-remainder)
                return f"(1/{2 * a_sq:.6g})*log(|(x+{shift:.6g}-{a_sq:.6g})/(x+{shift:.6g}+{a_sq:.6g})|)"
        except Exception:
            pass
    
    # ─── ∫e^(ax) * sin(bx) and ∫e^(ax) * cos(bx) ───
    match_exp_sin = re.match(r'^e\^\((-?[\d.]*)\*?x\)\*sin\(([\d.]*)\*?x\)$', m)
    if match_exp_sin:
        a = float(match_exp_sin.group(1)) if match_exp_sin.group(1) and match_exp_sin.group(1) != '-' else (
            -1.0 if match_exp_sin.group(1) == '-' else 1.0)
        b_val = float(match_exp_sin.group(2)) if match_exp_sin.group(2) else 1.0
        denom = a ** 2 + b_val ** 2
        return f"e^({a:.6g}*x)*({a:.6g}*sin({b_val:.6g}*x)-{b_val:.6g}*cos({b_val:.6g}*x))/{denom:.6g}"
    
    match_exp_cos = re.match(r'^e\^\((-?[\d.]*)\*?x\)\*cos\(([\d.]*)\*?x\)$', m)
    if match_exp_cos:
        a = float(match_exp_cos.group(1)) if match_exp_cos.group(1) and match_exp_cos.group(1) != '-' else (
            -1.0 if match_exp_cos.group(1) == '-' else 1.0)
        b_val = float(match_exp_cos.group(2)) if match_exp_cos.group(2) else 1.0
        denom = a ** 2 + b_val ** 2
        return f"e^({a:.6g}*x)*({a:.6g}*cos({b_val:.6g}*x)+{b_val:.6g}*sin({b_val:.6g}*x))/{denom:.6g}"
    
    return None


# ═══════════════════════════════════════════════════════════════
#  SECTION 4: THE NUMERIC SOLVER (hel_adadi) - Simpson's Rule
# ═══════════════════════════════════════════════════════════════

def qayyes_mo3adala(mo3adala: str, x: float) -> float:
    """
    Evaluate equation.
    Added LOGIC for LIMITS:
    - If 1/0 -> check limit -> return inf (bla maytplant)
    - If x/inf -> return 0
    """
    # 1. Handle Limits at Infinity logic directly
    if x == float('inf'):
        # Logic: any number / inf = 0
        # Logic: x * inf = inf
        try:
            # Try evaluating with a huge number to see behavior
            val_huge = 1e15
            res = qayyes_mo3adala(mo3adala, val_huge)
            if abs(res) < 1e-5: return 0.0  # Converges to 0
            if res > 1e5: return float('inf') # Diverges
            return res # Converges to constant
        except:
            return float('nan')

    # Prepare safe namespace
    bi2a_amina = {
        'x': x,
        'sin': math.sin, 'cos': math.cos, 'tan': math.tan,
        'log': math.log, 'ln': math.log, 'log10': math.log10,
        'exp': math.exp, 'sqrt': math.sqrt, 'pi': math.pi, 'e': math.e,
        'abs': abs,
        'asin': math.asin, 'acos': math.acos, 'atan': math.atan,
        # Helper lambdas for reciprocal trig functions
        'sec': lambda v: 1.0/math.cos(v),
        'csc': lambda v: 1.0/math.sin(v),
        'cot': lambda v: math.cos(v)/math.sin(v) if math.sin(v)!=0 else float('inf')
    }
    
    # Preprocess
    ta3bir = mo3adala.replace('^', '**')
    ta3bir = re.sub(r'\|([^|]+)\|', r'abs(\1)', ta3bir)
    ta3bir = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', ta3bir) # 2x -> 2*x
    ta3bir = re.sub(r'(\d)(\()', r'\1*\2', ta3bir)       # 2(x) -> 2*(x)
    ta3bir = re.sub(r'(\))([a-zA-Z0-9\(])', r'\1*\2', ta3bir) # )x -> )*x

    try:
        return float(eval(ta3bir, {"__builtins__": {}}, bi2a_amina))
        
    except ZeroDivisionError:
        # ─── HNA FIN KAIN L'INTELLIGENCE (Limit Logic) ───
        # Ila lqina 1/0, kanjrrbu x + 0.0000001 (Limit a droite)
        try:
            epsilon = 1e-9
            # Re-evaluate slightly to the right
            bi2a_amina['x'] = x + epsilon
            val_lim = float(eval(ta3bir, {"__builtins__": {}}, bi2a_amina))
            
            # Ila kanet kbira bzaf, rah l'infini
            if val_lim > 1e10:
                return float('inf')
            elif val_lim < -1e10:
                return float('-inf')
            else:
                return val_lim
        except:
            return float('inf') # Fallback to infinity
            
    except (ValueError, OverflowError):
        return float('nan')


def hel_adadi(mo3adala: str, b: float, n: float, k: int = 1000) -> Optional[float]:
    """
    Numeric Solver using Composite Simpson's Rule.
    hel = solve | adadi = numeric
    b = bidaya (start) | n = nihaya (end) | k = khatwa (steps)
    
    Simpson's Rule: ∫[a,b] f(x)dx ≈ (h/3)[f(x₀) + 4f(x₁) + 2f(x₂) + 4f(x₃) + ... + f(xₙ)]
    
    Must have even number of steps (k).
    """
    if k % 2 != 0:
        k += 1  # Simpson's needs even number of intervals
    
    h = (n - b) / k  # h = step size (toul_l_khatwa)
    
    if h == 0:
        return 0.0
    
    try:
        majmu3 = qayyes_mo3adala(mo3adala, b)  # sum starts with f(a)
        if math.isnan(majmu3):
            # Try shifting slightly to avoid singularities
            majmu3 = qayyes_mo3adala(mo3adala, b + h * 0.001)
        
        nihaya_qima = qayyes_mo3adala(mo3adala, n)
        if math.isnan(nihaya_qima):
            nihaya_qima = qayyes_mo3adala(mo3adala, n - h * 0.001)
        
        majmu3 += nihaya_qima
        
        khataat = 0  # error count
        
        for i in range(1, k):
            xi = b + i * h
            fi = qayyes_mo3adala(mo3adala, xi)
            
            if math.isnan(fi) or math.isinf(fi):
                # Try nearby point
                fi = qayyes_mo3adala(mo3adala, xi + h * 0.001)
                if math.isnan(fi) or math.isinf(fi):
                    fi = 0.0
                    khataat += 1
            
            if i % 2 == 1:
                majmu3 += 4 * fi  # Odd indices: multiply by 4
            else:
                majmu3 += 2 * fi  # Even indices: multiply by 2
        
        natija = majmu3 * h / 3
        
        if khataat > k * 0.1:  # More than 10% errors
            print(f"  ⚠️ Tanbih: {khataat}/{k} nuqat fiha mushkil (singularities)")
        
        return natija
    
    except Exception as khata2:
        print(f"  ❌ Khata2 f l-hesab l-adadi: {khata2}")
        return None


def hel_adadi_trapeze(mo3adala: str, b: float, n: float, k: int = 1000) -> Optional[float]:
    """
    Backup Numeric Solver using Trapezoidal Rule.
    Simpler but less accurate than Simpson's.
    
    ∫[a,b] f(x)dx ≈ (h/2)[f(x₀) + 2f(x₁) + 2f(x₂) + ... + f(xₙ)]
    """
    h = (n - b) / k
    
    if h == 0:
        return 0.0
    
    try:
        majmu3 = qayyes_mo3adala(mo3adala, b) + qayyes_mo3adala(mo3adala, n)
        
        for i in range(1, k):
            xi = b + i * h
            fi = qayyes_mo3adala(mo3adala, xi)
            if not (math.isnan(fi) or math.isinf(fi)):
                majmu3 += 2 * fi
        
        return majmu3 * h / 2
    except Exception:
        return None


def hel_adadi_romberg(mo3adala: str, b: float, n: float, martaba: int = 6) -> Optional[float]:
    """
    Romberg Integration - more accurate extrapolation method.
    Uses Richardson extrapolation on trapezoidal rule.
    
    martaba = order of extrapolation
    """
    # Build Romberg table
    jadwal_romberg = [[0.0] * (martaba + 1) for _ in range(martaba + 1)]
    
    try:
        # R(0,0) = basic trapezoidal
        h = n - b
        jadwal_romberg[0][0] = (h / 2) * (
                qayyes_mo3adala(mo3adala, b) + qayyes_mo3adala(mo3adala, n)
        )
        
        for i in range(1, martaba + 1):
            # Compute R(i,0) - Trapezoidal with 2^i intervals
            k = 2 ** i
            h = (n - b) / k
            
            majmu3_jadid = 0.0
            for j in range(1, k, 2):  # Only new midpoints
                xj = b + j * h
                fi = qayyes_mo3adala(mo3adala, xj)
                if not (math.isnan(fi) or math.isinf(fi)):
                    majmu3_jadid += fi
            
            jadwal_romberg[i][0] = jadwal_romberg[i - 1][0] / 2 + h * majmu3_jadid
            
            # Richardson extrapolation
            for j in range(1, i + 1):
                mu3amil_4 = 4 ** j
                jadwal_romberg[i][j] = (
                                               mu3amil_4 * jadwal_romberg[i][j - 1] - jadwal_romberg[i - 1][j - 1]
                                       ) / (mu3amil_4 - 1)
        
        return jadwal_romberg[martaba][martaba]
    except Exception:
        return None


def hel_adadi_gauss_legendre(mo3adala: str, b: float, n: float, nuqat: int = 5) -> Optional[float]:
    """
    Gauss-Legendre Quadrature - very accurate for smooth functions.
    Uses pre-computed nodes and weights.
    
    nuqat = number of quadrature points (up to 5)
    """
    # Gauss-Legendre nodes and weights for [-1, 1]
    jadwal_gauss = {
        2: {
            'nuqat': [-0.5773502691896257, 0.5773502691896257],
            'awzan': [1.0, 1.0]
        },
        3: {
            'nuqat': [-0.7745966692414834, 0.0, 0.7745966692414834],
            'awzan': [0.5555555555555556, 0.8888888888888888, 0.5555555555555556]
        },
        4: {
            'nuqat': [-0.8611363115940526, -0.3399810435848563,
                      0.3399810435848563, 0.8611363115940526],
            'awzan': [0.3478548451374538, 0.6521451548625461,
                      0.6521451548625461, 0.3478548451374538]
        },
        5: {
            'nuqat': [-0.9061798459386640, -0.5384693101056831, 0.0,
                      0.5384693101056831, 0.9061798459386640],
            'awzan': [0.2369268850561891, 0.4786286704993665, 0.5688888888888889,
                      0.4786286704993665, 0.2369268850561891]
        }
    }
    
    if nuqat not in jadwal_gauss:
        nuqat = 5
    
    try:
        # Transform from [-1,1] to [b,n]: x = (b+n)/2 + (n-b)/2 * t
        wassat = (b + n) / 2  # midpoint
        nisf_toul = (n - b) / 2  # half-width
        
        majmu3 = 0.0
        for t, w in zip(jadwal_gauss[nuqat]['nuqat'], jadwal_gauss[nuqat]['awzan']):
            xi = wassat + nisf_toul * t
            fi = qayyes_mo3adala(mo3adala, xi)
            if not (math.isnan(fi) or math.isinf(fi)):
                majmu3 += w * fi
        
        return nisf_toul * majmu3
    except Exception:
        return None


def hel_adadi_monte_carlo(mo3adala: str, b: float, n: float, adad_nuqat: int = 100000) -> Optional[float]:
    """
    Monte Carlo Integration - useful for high dimensions or rough functions.
    adad_nuqat = number of random points
    
    ∫[a,b] f(x)dx ≈ (b-a)/N * Σ f(xᵢ)  where xᵢ are random in [a,b]
    """
    import random
    
    try:
        toul = n - b  # length of interval
        majmu3 = 0.0
        adad_salih = 0  # valid count
        
        for _ in range(adad_nuqat):
            xi = b + random.random() * toul
            fi = qayyes_mo3adala(mo3adala, xi)
            if not (math.isnan(fi) or math.isinf(fi)):
                majmu3 += fi
                adad_salih += 1
        
        if adad_salih == 0:
            return None
        
        return toul * majmu3 / adad_salih
    except Exception:
        return None


# ═══════════════════════════════════════════════════════════════
#  SECTION 5: DISPLAY HELPERS
# ═══════════════════════════════════════════════════════════════

def ard_sha3ar():
    """Display the banner. ard = display | sha3ar = banner"""
    print("""
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║   🔢  ╔╗╔╗  HYBRID INTEGRAL SOLVER  ╔╗╔╗  🔢                       ║
║       ╠╣╠╣  ── Moroccan Darija Ed. ── ╠╣╠╣                          ║
║       ╚╝╚╝                           ╚╝╚╝                          ║
║                                                                      ║
║   📐 Symbolic Logic (Ramzi) → Numeric Fallback (3Adadi)             ║
║   📚 Taylor Series (DL) + Advanced Techniques (Turuq Mutaqaddima)   ║
║   🇲🇦 Variable Names in Darija                                      ║
║                                                                      ║
║   Commands: 'dl' = Show DL table | 'turuq' = Show techniques        ║
║             'jadwal' = Integration table | 'khrouj' = Exit           ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
    """)


def ard_jadwal_takamol():
    """Display the complete integration table."""
    print("""
╔══════════════════════════════════════════════════════════════════╗
║              📋 JADWAL L-TAKAMOLAT (Integration Table)          ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║  ── ASASIYAT (Basics) ──────────────────────────────────────     ║
║  ∫ a dx           = a·x + C                                     ║
║  ∫ x dx           = x²/2 + C                                    ║
║  ∫ x^n dx         = x^(n+1)/(n+1) + C    [n ≠ -1]              ║
║  ∫ 1/x dx         = ln|x| + C                                   ║
║  ∫ e^x dx         = e^x + C                                     ║
║  ∫ a^x dx         = a^x/ln(a) + C                               ║
║  ∫ √x dx          = (2/3)·x^(3/2) + C                           ║
║  ∫ 1/√x dx        = 2·√x + C                                    ║
║                                                                  ║
║  ── TRIGONOMÉTRIQUE ─────────────────────────────────────────    ║
║  ∫ sin(x) dx      = -cos(x) + C                                 ║
║  ∫ cos(x) dx      = sin(x) + C                                  ║
║  ∫ tan(x) dx      = -ln|cos(x)| + C                             ║
║  ∫ cot(x) dx      = ln|sin(x)| + C                              ║
║  ∫ sec(x) dx      = ln|sec(x)+tan(x)| + C                      ║
║  ∫ csc(x) dx      = -ln|csc(x)+cot(x)| + C                     ║
║  ∫ sec²(x) dx     = tan(x) + C                                  ║
║  ∫ csc²(x) dx     = -cot(x) + C                                 ║
║  ∫ sec(x)tan(x)   = sec(x) + C                                  ║
║  ∫ csc(x)cot(x)   = -csc(x) + C                                 ║
║                                                                  ║
║  ── TRIG POWERS ──────────────────────────────────────────────   ║
║  ∫ sin²(x) dx     = x/2 - sin(2x)/4 + C                        ║
║  ∫ cos²(x) dx     = x/2 + sin(2x)/4 + C                        ║
║  ∫ sin³(x) dx     = -cos(x) + cos³(x)/3 + C                    ║
║  ∫ cos³(x) dx     = sin(x) - sin³(x)/3 + C                     ║
║  ∫ tan²(x) dx     = tan(x) - x + C                              ║
║                                                                  ║
║  ── INVERSE TRIG ─────────────────────────────────────────────   ║
║  ∫ 1/(1+x²) dx    = arctan(x) + C                               ║
║  ∫ 1/√(1-x²) dx   = arcsin(x) + C                               ║
║  ∫ arctan(x) dx   = x·arctan(x) - ln(1+x²)/2 + C               ║
║  ∫ arcsin(x) dx   = x·arcsin(x) + √(1-x²) + C                  ║
║                                                                  ║
║  ── LOGARITHMIC ──────────────────────────────────────────────   ║
║  ∫ ln(x) dx       = x·ln(x) - x + C                             ║
║  ∫ (ln(x))² dx    = x·(ln(x))² - 2x·ln(x) + 2x + C            ║
║  ∫ ln(x)/x dx     = (ln(x))²/2 + C                              ║
║  ∫ ln(1+x) dx     = (1+x)·ln(1+x) - x + C                      ║
║                                                                  ║
║  ── EXPONENTIAL PRODUCTS ─────────────────────────────────────   ║
║  ∫ x·e^x dx       = (x-1)·e^x + C                               ║
║  ∫ x²·e^x dx      = (x²-2x+2)·e^x + C                          ║
║  ∫ e^x·sin(x) dx  = e^x·(sin(x)-cos(x))/2 + C                  ║
║  ∫ e^x·cos(x) dx  = e^x·(sin(x)+cos(x))/2 + C                  ║
║                                                                  ║
║  ── HYPERBOLIC ───────────────────────────────────────────────   ║
║  ∫ sinh(x) dx     = cosh(x) + C                                 ║
║  ∫ cosh(x) dx     = sinh(x) + C                                 ║
║  ∫ tanh(x) dx     = ln(cosh(x)) + C                             ║
║                                                                  ║
║  ── SPECIAL FORMS ────────────────────────────────────────────   ║
║  ∫ 1/(x²+a²) dx   = (1/a)·arctan(x/a) + C                      ║
║  ∫ 1/(x²-a²) dx   = (1/2a)·ln|(x-a)/(x+a)| + C                 ║
║  ∫ √(1-x²) dx     = (x·√(1-x²) + arcsin(x))/2 + C             ║
║  ∫ √(x²+1) dx     = (x·√(x²+1) + ln(x+√(x²+1)))/2 + C        ║
║  ∫ 1/(1+e^x) dx   = x - ln(1+e^x) + C                          ║
║                                                                  ║
║  ── LINEAR COMPOSITION: f(ax+b) ──────────────────────────────   ║
║  ∫ f(ax+b) dx     = F(ax+b)/a + C     [F = antiderivative of f] ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
    """)


def ard_turuq():
    """Display available advanced techniques."""
    print("\n" + "═" * 60)
    print("  🧮 TURUQ MUTAQADDIMA (Advanced Integration Techniques)")
    print("═" * 60)
    
    turuq = TuruqMutaqaddima
    
    print("\n" + turuq.takamol_ajza2("ln(x)", "x"))
    print("\n" + turuq.ta8yir_muta8ayir_sharh("sqrt(1-x^2)", "sin(θ)"))
    print("\n" + turuq.kusur_juz2iya("1", [("1", 1), ("-1", 1)]))
    print("\n" + turuq.ta8yir_trigonometrique("a2-x2"))
    print("\n" + turuq.ta8yir_trigonometrique("a2+x2"))
    print("\n" + turuq.ta8yir_trigonometrique("x2-a2"))
    print("\n" + turuq.weierstrass("1/(2+sin(x))"))
    print("\n" + turuq.formule_reduction_sin(4))
    print("\n" + turuq.formule_reduction_cos(3))
    print("\n" + turuq.formule_reduction_tan(4))
    print("\n" + turuq.formule_reduction_x_n_exp(3))
    print("\n" + turuq.formule_reduction_ln_n(2))
    print("\n" + turuq.takamol_feynman_sharh())
    
    print("\n" + "═" * 60 + "\n")


# ═══════════════════════════════════════════════════════════════
#  SECTION 6: STUDENT STYLE MAIN LOOP (Authentic)
# ═══════════════════════════════════════════════════════════════

def ard_sha3ar():
    """Simple header, student style"""
    print("\n")
    print("--------------------------------------------------")
    print(" INTEGRAL SOLVER - PFE Project v1.0")
    print("--------------------------------------------------")

def tanfid_ra2isi():
    """
    Main execution loop.
    Style: Darija + Français technique (Student style).
    """
    ard_sha3ar()
    
    while True:
        print("\n")
        # Input style simple
        print("Dkhel l'equation f(x) (ola 'exit'):")
        mo3adala = input(" >> ").strip()
        
        if not mo3adala: continue
        if mo3adala.lower() in ('exit', 'q', 'quitter'):
            print("\nBslama! Bon courage.")
            break
        
        # Shortcuts
        if mo3adala.lower() == 'dl': JadwalDL.ard_kol_dl(); continue
        if mo3adala.lower() == 'table': ard_jadwal_takamol(); continue
        if mo3adala.lower() == 'help': 
            print("  Commandes: dl, table, exit")
            continue
        
        try:
            print("Les bornes [a, b] (inf = l'infini):")
            b_str = input("  a (debut): ").strip()
            n_str = input("  b (fin):   ").strip()
            
            # Safe eval for pi/e
            safe_env = {'pi': math.pi, 'e': math.e, 'inf': float('inf')}
            b = float(eval(b_str.replace('^', '**'), {"__builtins__":{}}, safe_env))
            n = float(eval(n_str.replace('^', '**'), {"__builtins__":{}}, safe_env))
            
            # --- Handling Infinity (Numeric Trick) ---
            LIMIT = 500.0
            b_calc, n_calc = b, n
            is_inf = False
            
            if n == float('inf'): n_calc = LIMIT; is_inf = True
            if b == float('-inf'): b_calc = -LIMIT; is_inf = True
                
        except:
            print("  [!] Erreur f les bornes. 3awd dakhul ar9am.")
            continue
        
        print("-" * 40)
        print(f"Calcul de l'integral de {b_str} a {n_str}...")
        
        # ─── 1. SYMBOLIC SOLVER ───
        print("  [1] Recherche de la primitive (Symbolique)...")
        natija_ramziya = hel_ramzi(mo3adala)
        
        has_formula = False
        if natija_ramziya:
            has_formula = True
            # Hna l'affichage "Humain" li bghiti
            print(f"      => F(x) = {natija_ramziya} + C")
            
            try:
                val_n = qayyes_mo3adala(natija_ramziya, n_calc)
                val_b = qayyes_mo3adala(natija_ramziya, b_calc)
                if not (math.isnan(val_n) or math.isnan(val_b)):
                    exact = val_n - val_b
                    print(f"      => Resultat Exact: {exact:.6f}")
            except: pass
        else:
            print("      [!] Pas de formule simple trouvee.")

        # ─── 2. NUMERIC SOLVER ───
        print("  [2] Verification Numerique...")
        
        # FIX: Pre-process equation for numeric solver to handle sin^2(x)
        # Python needs sin(x)**2, not sin^2(x)
        # Simple regex fix for common trig powers before sending to numeric
        mo3adala_num = mo3adala
        mo3adala_num = re.sub(r'(sin|cos|tan)\^(\d+)\((.+?)\)', r'(\1(\3)**\2)', mo3adala_num)
        
        # Only run numeric if not infinite bounds OR if we clamped them
        res_simp = hel_adadi(mo3adala_num, b_calc, n_calc, k=20000)
        res_romb = hel_adadi_romberg(mo3adala_num, b_calc, n_calc, martaba=10)
        
        final_res = None
        if res_romb is not None and not math.isnan(res_romb):
            final_res = res_romb
            print(f"      => Romberg : {res_romb:.6f}")
        elif res_simp is not None and not math.isnan(res_simp):
            final_res = res_simp
            print(f"      => Simpson : {res_simp:.6f}")
        else:
            print("      [!] Erreur de calcul (Singularity/NaN).")

        # ─── FINAL CONCLUSION ───
        print("-" * 40)
        if final_res is not None:
            print(f" RESULTAT FINAL: {final_res:.6f}")
        elif has_formula:
            print(" RESULTAT FINAL: Voir la formule ci-dessus.")
        else:
            print(" Echec du calcul.")


# ═══════════════════════════════════════════════════════════════
#  ENTRY POINT
# ═══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    try:
        tanfid_ra2isi()
    except KeyboardInterrupt:
        print("\n\n  👋 Bslama! (Ctrl+C pressed)\n")
    except Exception as khata2_3amm:
        print(f"\n  ❌ Khata2 3amm: {khata2_3amm}")
        import traceback
        traceback.print_exc()
import os
from distributions import (
    bernoulli,
    beta,
    binomial,
    cauchy,
    chi_squared,
    dirichlet,
    exponential,
    exponential_exp1,
    fisher_f,
    frechet,
    gamma,
    geometric,
    gumbel,
    hypergeometric,
    inverse_gaussian,
    log_normal,
    normal,
    normal_inverse_gaussian,
    pareto,
    pert,
    poisson,
    skew_normal,
    standard_geometric,
    standard_normal,
    student_t,
    triangular,
    unit_ball,
    unit_circle,
    unit_disc,
    unit_sphere,
    weibull,
    zeta,
    zipf,
)

if __name__ == "__main__":
    out = "charts"
    ext = "svg"
    if not os.path.exists(out):
        os.makedirs(out)
    for distr in (
        bernoulli,
        beta,
        binomial,
        cauchy,
        chi_squared,
        dirichlet,
        exponential,
        exponential_exp1,
        fisher_f,
        frechet,
        gamma,
        geometric,
        gumbel,
        hypergeometric,
        inverse_gaussian,
        log_normal,
        normal,
        normal_inverse_gaussian,
        pareto,
        pert,
        poisson,
        skew_normal,
        standard_geometric,
        standard_normal,
        student_t,
        triangular,
        unit_ball,
        unit_circle,
        unit_disc,
        unit_sphere,
        weibull,
        zeta,
        zipf,
    ):
        distr.save_to(out, ext)

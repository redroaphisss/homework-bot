"""
Bond pricing calculations for fixed income assignment.
Includes zero-coupon and coupon bond pricing, duration, convexity.
"""

import numpy as np
from typing import List, Tuple


def discount_factor(rate: float, time: float, compounding: str = "semi_annual") -> float:
    """
    Calculate discount factor for a given rate and time.

    Parameters
    ----------
    rate : float
        Annual interest rate (decimal, e.g., 0.05 for 5%)
    time : float
        Time to maturity in years
    compounding : str
        Compounding frequency: 'annual', 'semi_annual', 'continuous'

    Returns
    -------
    float
        Discount factor
    """
    if compounding == "annual":
        return 1.0 / (1.0 + rate) ** time
    elif compounding == "semi_annual":
        return 1.0 / (1.0 + rate / 2) ** (2 * time)
    elif compounding == "continuous":
        return np.exp(-rate * time)
    else:
        raise ValueError(f"Unknown compounding: {compounding}")


def zero_coupon_price(face: float, rate: float, time: float,
                     compounding: str = "semi_annual") -> float:
    """
    Price of a zero-coupon bond.

    Parameters
    ----------
    face : float
        Face value
    rate : float
        Annual interest rate (decimal)
    time : float
        Time to maturity in years
    compounding : str
        Compounding frequency

    Returns
    -------
    float
        Present value of zero-coupon bond
    """
    df = discount_factor(rate, time, compounding)
    return face * df


def coupon_bond_price(coupon_rate: float, face: float, times: List[float],
                      zero_rates: List[float], compounding: str = "semi_annual") -> float:
    """
    Price a coupon bond using zero rates for each cash flow.

    Parameters
    ----------
    coupon_rate : float
        Annual coupon rate (decimal)
    face : float
        Face value
    times : List[float]
        Times to each cash flow in years (including final principal)
    zero_rates : List[float]
        Zero rates for each cash flow time (same length as times)
    compounding : str
        Compounding frequency

    Returns
    -------
    float
        Bond price
    """
    if len(times) != len(zero_rates):
        raise ValueError("times and zero_rates must have same length")

    coupon = coupon_rate * face / 2  # semi-annual coupon
    price = 0.0

    for t, r in zip(times[:-1], zero_rates[:-1]):
        price += coupon * discount_factor(r, t, compounding)

    # Last cash flow includes coupon and face
    price += (coupon + face) * discount_factor(zero_rates[-1], times[-1], compounding)

    return price


def modified_duration(coupon_rate: float, face: float, times: List[float],
                      zero_rates: List[float], compounding: str = "semi_annual") -> float:
    """
    Calculate modified duration of a coupon bond using zero curve.

    Parameters
    ----------
    coupon_rate : float
        Annual coupon rate (decimal)
    face : float
        Face value
    times : List[float]
        Times to each cash flow in years
    zero_rates : List[float]
        Zero rates for each cash flow time
    compounding : str
        Compounding frequency

    Returns
    -------
    float
        Modified duration (in years)
    """
    if len(times) != len(zero_rates):
        raise ValueError("times and zero_rates must have same length")

    coupon = coupon_rate * face / 2
    price = 0.0
    weighted_time_sum = 0.0

    for t, r in zip(times[:-1], zero_rates[:-1]):
        df = discount_factor(r, t, compounding)
        price += coupon * df
        weighted_time_sum += coupon * df * t

    # Last cash flow
    df_last = discount_factor(zero_rates[-1], times[-1], compounding)
    price += (coupon + face) * df_last
    weighted_time_sum += (coupon + face) * df_last * times[-1]

    if price == 0:
        return 0.0

    return weighted_time_sum / price


def convexity(coupon_rate: float, face: float, times: List[float],
              zero_rates: List[float], compounding: str = "semi_annual") -> float:
    """
    Calculate convexity of a coupon bond using zero curve.

    Parameters
    ----------
    coupon_rate : float
        Annual coupon rate (decimal)
    face : float
        Face value
    times : List[float]
        Times to each cash flow in years
    zero_rates : List[float]
        Zero rates for each cash flow time
    compounding : str
        Compounding frequency

    Returns
    -------
    float
        Convexity (in years^2)
    """
    if len(times) != len(zero_rates):
        raise ValueError("times and zero_rates must have same length")

    coupon = coupon_rate * face / 2
    price = 0.0
    weighted_time_sq_sum = 0.0

    for t, r in zip(times[:-1], zero_rates[:-1]):
        df = discount_factor(r, t, compounding)
        price += coupon * df
        weighted_time_sq_sum += coupon * df * (t ** 2)

    # Last cash flow
    df_last = discount_factor(zero_rates[-1], times[-1], compounding)
    price += (coupon + face) * df_last
    weighted_time_sq_sum += (coupon + face) * df_last * (times[-1] ** 2)

    if price == 0:
        return 0.0

    return weighted_time_sq_sum / price


def price_change_approx(price: float, modified_duration: float,
                        convexity: float, delta_y: float) -> Tuple[float, float]:
    """
    Approximate price change using duration and convexity.

    Parameters
    ----------
    price : float
        Initial bond price
    modified_duration : float
        Modified duration (years)
    convexity : float
        Convexity (years^2)
    delta_y : float
        Change in yield (decimal)

    Returns
    -------
    Tuple[float, float]
        (dollar change, percentage change)
    """
    pct_change = -modified_duration * delta_y + 0.5 * convexity * (delta_y ** 2)
    dollar_change = price * pct_change
    return dollar_change, pct_change


def zero_coupon_modified_duration(rate: float, time: float,
                                  compounding: str = "annual") -> float:
    """
    Modified duration of a zero-coupon bond.

    Parameters
    ----------
    rate : float
        Annual yield (decimal)
    time : float
        Time to maturity (years)
    compounding : str
        Compounding frequency

    Returns
    -------
    float
        Modified duration (years)
    """
    if compounding == "annual":
        return time / (1 + rate)
    elif compounding == "semi_annual":
        return time / (1 + rate / 2)
    elif compounding == "continuous":
        return time
    else:
        raise ValueError(f"Unknown compounding: {compounding}")


if __name__ == "__main__":
    # Simple test
    print("Testing bond pricing functions...")

    # Test discount factors
    df_semi = discount_factor(0.05, 1.0, "semi_annual")
    df_ann = discount_factor(0.05, 1.0, "annual")
    print(f"Discount factor semi-annual 5% 1yr: {df_semi:.6f}")
    print(f"Discount factor annual 5% 1yr: {df_ann:.6f}")

    # Zero coupon price
    zc_price = zero_coupon_price(100, 0.05, 1.0, "semi_annual")
    print(f"Zero-coupon bond price: {zc_price:.6f}")
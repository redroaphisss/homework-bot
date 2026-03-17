---
name: bond-pricing
description: Use when pricing bonds.
argument-hint: "[action]"
---

# Bond Pricing Guide

This skill provides bond pricing calculations for fixed income assignments. Use it when you need to compute bond prices, durations, convexities, or approximate price changes.

## Available Functions

The `bond_pricing.py` script in `scripts/` provides the following functions:

- `discount_factor(rate, time, compounding="semi_annual")` – Compute discount factor for given rate and time.
- `zero_coupon_price(face, rate, time, compounding="semi_annual")` – Price of a zero-coupon bond.
- `coupon_bond_price(coupon_rate, face, times, zero_rates, compounding="semi_annual")` – Price a coupon bond using zero rates for each cash flow.
- `modified_duration(coupon_rate, face, times, zero_rates, compounding="semi_annual")` – Modified duration of a coupon bond.
- `convexity(coupon_rate, face, times, zero_rates, compounding="semi_annual")` – Convexity of a coupon bond.
- `price_change_approx(price, modified_duration, convexity, delta_y)` – Approximate price change using duration and convexity.
- `zero_coupon_modified_duration(rate, time, compounding="annual")` – Modified duration of a zero-coupon bond.

All rates are in decimal form (e.g., 0.05 for 5%). Time is in years. Compounding options: `"annual"`, `"semi_annual"`, `"continuous"`.

## Quick Examples

### Python Usage

```python
from bond_pricing import discount_factor, zero_coupon_price, coupon_bond_price

# Discount factor
df = discount_factor(0.05, 1.0, "semi_annual")
print(f"Discount factor: {df:.6f}")

# Zero-coupon bond price
price_zc = zero_coupon_price(100, 0.05, 1.0, "semi_annual")
print(f"Zero-coupon price: {price_zc:.6f}")

# Coupon bond with zero curve
times = [0.5, 1.0, 1.5, 2.0]
zero_rates = [0.04, 0.042, 0.045, 0.048]
price_cb = coupon_bond_price(0.05, 100, times, zero_rates, "semi_annual")
print(f"Coupon bond price: {price_cb:.6f}")
```

### Running the Script

You can run the script directly to see a simple test:

```bash
uv run python .claude/skills/bond-pricing/scripts/bond_pricing.py
```

## Steps

1. **Identify the task**: Determine what needs to be calculated (bond price, duration, convexity, price change approximation, etc.).

2. **Gather inputs**: Collect all necessary parameters (face value, coupon rate, times to cash flows, zero rates, compounding convention). Ensure rates are in decimal form, times in years.

3. **Compute** using the chosen function. Validate input lengths match where required.

4. **Export results**. Save both inputs and outputs in a clear format (CSV, text, or JSON). Include a timestamp and a brief description.

5. **Verify**: If feasible, cross‑check with an alternative calculation or manual estimate.

## Common Scenarios

### Pricing a Zero‑Coupon Bond
Given face value $100, yield 5% (semi‑annual compounding), maturity 2 years:
```python
price = zero_coupon_price(100, 0.05, 2.0, "semi_annual")
```

### Pricing a Coupon Bond with a Zero Curve
Assume semi‑annual coupons, coupon rate 6%, face $100, cash flows at 0.5, 1.0, 1.5, 2.0 years with zero rates 4%, 4.2%, 4.5%, 4.8%:
```python
times = [0.5, 1.0, 1.5, 2.0]
zero_rates = [0.04, 0.042, 0.045, 0.048]
price = coupon_bond_price(0.06, 100, times, zero_rates, "semi_annual")
```

### Computing Duration and Convexity
Using the same cash flows and zero rates:
```python
dur = modified_duration(0.06, 100, times, zero_rates, "semi_annual")
conv = convexity(0.06, 100, times, zero_rates, "semi_annual")
```

### Approximating Price Change for a Yield Shift
If the bond’s price is $105.50, modified duration 4.2 years, convexity 25.0, and the yield increases by 10 bps (0.001):
```python
dollar_change, pct_change = price_change_approx(105.50, 4.2, 25.0, 0.001)
```

## Notes

- The coupon bond pricing function assumes semi‑annual coupon payments (coupon = coupon_rate * face / 2). If the bond pays annual coupons, adjust the coupon amount accordingly.
- For zero‑coupon bonds, the zero‑coupon modified duration formula depends on compounding convention; the function handles this.
- Always validate input lengths: `times` and `zero_rates` must have the same length.
- When exporting results, include a timestamp and a brief description of the input parameters.



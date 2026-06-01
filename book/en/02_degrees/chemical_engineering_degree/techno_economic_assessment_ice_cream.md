# Techno-Economic Assessment of Ice Cream Manufacture at Different Production Scales

## Introduction

Sustainability has become a critical factor in the design of food manufacturing systems. In particular, the ice cream industry combines characteristics that make it ideal for studying the viability of different production paradigms:

1. **Product Complexity**: A frozen multiphase product (water-oil emulsion with ice crystals)
2. **Wide Range of Scales**: From home-made production to large industrial plants
3. **Commercial Relevance**: Artisanal and industrial business models coexist in the same market
4. **Energy Intensity**: Accounts for 11-14% of total energy in a cradle-to-grave approach

In this chapter, we explore how **model-based process engineering** can help us compare the economic and environmental viability of different ice cream production scenarios, from home manufacturing to large industrial plants.

---

## Learning Objectives

Upon completion of this chapter, you will be able to:

- Understand **mass and energy balances** in ice cream production at different scales
- Evaluate the **economic viability** of different food business models
- Estimate **energy consumption and carbon footprint** of food processes
- Apply **sensitivity analysis** to account for uncertainties in raw materials and energy
- Identify the **scale break-even points** where a business model becomes profitable

---

## Production Scenarios Analyzed

The study presents five different production scenarios, classified by their degree of decentralization and production scale:

```{figure} techno_economic_assessment_ice_cream_images/page4_img1.jpeg
---
width: 90%
align: center
name: fig-ice-cream-flowsheet-en
---
Ice cream plant production flow sheet depicting all the steps of the industrial process. Both batch and continuous pasteurisation alternatives are shown.
```

### Industrial Production

#### Single Plant (SP)

- **Scale**: 650 - 3,325 kg/h
- **Operation**: 5 days/week, 2 shifts
- **Characteristics**: High specialization, significant economies of scale
- **Pasteurization type**: 
  - Batch: $T_{\text{past}} = 69.4°C$, $t > 30$ min (production < 600 l/h)
  - Continuous: $T_{\text{past}} = 79.4°C$, $t > 15$ s (with heat regeneration)

#### Multi-Plant (MP)

- **Scale**: > 3,325 kg/h total (distributed as plants of ~3,330 kg/h each)
- **Key Advantage**: Reduction of transport and storage costs through decentralization

### Artisanal Production

#### Home Manufacturing (HM)

- **Scale**: < 3 kg/h per installation
- **Operation**: 5 days/week, 1 shift (gig-economy model)
- **Equipment**: Domestic kitchen equipment
- **Profitability**: Profitable below 45 kg/h total production

#### Food Incubator (FI)

- **Scale**: ~8.7 kg/h per installation
- **Model**: Specialized equipment shared by freelance workers
- **Advantage**: No capital investment needed (only working capital)
- **Profitability**: Viable between 45 - 650 kg/h

#### Distributed Manufacturing (DM)

- **Scale**: ~21.8 kg/h per installation (modular equipment)
- **Model**: Small catering-sized facilities distributed geographically
- **Management**: Two variants - low-level (franchise) and high-level (corporate)
- **Profitability**: Viable between 650 - 3,325 kg/h

### Detailed Description of Artisanal Processes

Artisanal processes (HM, FI, DM) drastically reduce the complexity of unit operations compared to industrial plants, adapting technology to domestic or semi-industrial capacities.

```{figure} techno_economic_assessment_ice_cream_images/page6_img1.jpeg
---
width: 100%
align: center
name: fig-artisanal-flowsheets-en
---
Artisanal manufacture flow chart for (a) Distributed Manufacturing (DM) and (b) Food Incubator (FI) and Home Manufacturing (HM). The industrial unit operations were down-scaled as domestic kitchen batch processes.
```

#### Operational Characteristics of Artisanal Methods

**Home Manufacturing (HM)**: Uses modified domestic kitchen equipment. The process flow includes:
- **Mixing**: Standard containers (5-10 l) with manual agitation or domestic blender
- **Pasteurization**: Thermal water bath at controlled temperature (~69°C, 30 min) or domestic pasteurizer
- **Homogenization**: High-speed domestic blender (mechanical emulsification)
- **Cooling**: Domestic refrigerator (4-8 hours) or ice-based home cooling tunnel
- **Freezing**: Domestic ice cream machine (Carpigiani-type, ~2-3 l/batch, 20-40 min)
- **Hardening**: Domestic freezer (-18°C, 2-4 hours)

**Food Incubator (FI)**: Specialized but shared equipment among workers. Improvements over HM:
- Laboratory pasteurizer (10-20 l, precise T/t control)
- Laboratory homogenizer (higher emulsification efficiency)
- Semi-commercial ice cream machine (5-10 l/h, overrun control)
- Dedicated cooling tunnel (reduced time to 1-2 hours)
- Savings through economies of scale in shared inputs

**Distributed Manufacturing (DM)**: Modular equipment transferable between locations. Distinctive features:
- Continuous freezing system (higher throughput, 15-25 kg/h)
- Automated hardening tunnel
- Reduced total process time (6-10 hours vs 12-20 in HM/FI)
- Greater batch-to-batch consistency through sensor-based control

---

## Ice Cream Formulations Studied

### Standard Ice Cream

Typical composition of industrial standard ice cream (vanilla and chocolate flavors):

| Ingredient | Mass Fraction | Function |
|---|---|---|
| Coconut oil | 0.150 | Base fat |
| Skimmed milk powder | 0.120 | Milk solids |
| Sugar | 0.100 | Primary sweetener |
| Glucose syrup | 0.030 | Secondary sweetener |
| Guar gum | 0.002 | Stabilizer |
| Carrageenan | 0.001 | Stabilizer |
| Monoglycerides | 0.002 | Emulsifier |
| Water | 0.545 | Solvent |
| Cocoa powder (chocolate) | 0.030 | Flavor |

**Key Parameters**:
- Overrun: 110%
- Final composition: Fat 7%, Protein 0.6%, Carbohydrates 36%, Water 60.3%

### Premium Ice Cream

Higher quality ingredients (banana flavor with chocolate chunks and walnuts):

| Ingredient | Mass Fraction |
|---|---|
| Cream (40% fat) | 0.250 |
| Condensed skim milk | 0.272 |
| Sugar | 0.100 |
| Molasses | 0.060 |
| Egg yolk powder | 0.010 |
| Soya lecithin | 0.002 |
| Banana puree | 0.075 |
| Chocolate chunks | 0.085 |
| Walnuts | 0.055 |

**Key Parameters**:
- Overrun: 27%
- Final composition: Fat 42.9%, Protein 7.1%, Carbohydrates 47.6%, Water 2.4%

---

## Mathematical Modeling of Thermophysical Properties

For each formulation, we calculate properties that vary with temperature using mixing rules based on main components.

### Initial Freezing Point (TIF)

$$T_{\text{IF}} = 9.4915 \times 10^{-5} \left( \sum \frac{x_k M_{\text{sucrose}}}{M_k} \cdot 100 \right)^2 + 6.1231 \times 10^{-2} \left( \sum \frac{x_k M_{\text{sucrose}}}{M_k} \cdot 100 \right) + \frac{x_{\text{MSNF}} \times (-2.37)}{x_w}$$

where:
- $x_k$: mass fraction of component $k$
- $x_w$: water mass fraction
- $x_{\text{MSNF}}$: milk solids non-fat fraction

### Ice Fraction

$$x_{\text{ice}}(T) = x_w \left( 1 - \frac{T_{\text{IF}}}{T} \right)$$

### Specific Heat

$$c_p = \sum_j x_j c_{p,j} - L_f\left(T_{\text{IF}}\right) \frac{dx_{\text{ice}}}{dT}$$

where $L_f = 333.8 + 2.1165 \cdot T$ is the latent heat of fusion in kJ/kg.

### Overrun

$$Ov_{\text{ic}} = \frac{V_{\text{aerated}} - V_{\text{non-aerated}}}{V_{\text{non-aerated}}} \times 100\%$$

Overrun increases total volume by incorporating air as small bubbles. It is critical for texture and final sales volume.

---

## Unit Cost Analysis

One of the key results of the study is how unit costs ($/kg) vary across production scales:

```{figure} techno_economic_assessment_ice_cream_images/page8_img1.jpeg
---
width: 100%
align: center
name: fig-unit-costs-en
---
Variation of the unit cost ($/kg) for different manufacturing scales: (a) premium ice cream sold in 500 ml packages, (b) premium ice cream sold in 150 ml packages and (c) standard ice cream sold in 1000 ml packages. Shaded areas represent the trust region set by the uncertainties.
```

### Viability Regions

Cost curves can be divided into three regions:

1. **Non-Viable Region**: Very high costs at low capacities; steep slope
2. **Transition Region**: Visible economies of scale; significant cost reduction
3. **Plateau Region**: Additional capacity increases do not improve unit costs (equipment saturation)

### Key Findings

- **HM is profitable** below 45 kg/h (cost < market price)
- **DM with low management** is more competitive than HM/FI at intermediate productions (100-1,000 kg/h)
- **SP requires minimum 650 kg/h** to be profitable
- **Multiple plants** improve margins at productions > 3,325 kg/h

---

## Energy Consumption Analysis

Energy consumption is a critical factor for process sustainability.

```{figure} techno_economic_assessment_ice_cream_images/page9_img1.jpeg
---
width: 100%
align: center
name: fig-energy-consumption-en
---
(a) Energy consumption for a single plant (SP) scenario. A discontinuity - pointed out with an arrow - appears when the process shifts from batch to continuous pasteurisation, which enables heat regeneration. (b) Energy consumption for HM, FI and DM. The integer constraints for processing equipment cause discontinuities in the energy plot. Minimum consumption is achieved when operating at full capacity.
```

### Energy Consumption in Industrial Plants

For a single plant (SP):

$$E_{\text{total}} = E_{\text{heating}} + E_{\text{cooling}} + E_{\text{freezing}} + E_{\text{pumping}}$$

**Typical Values**:
- Batch → continuous transition (600 l/h): ~15% saving through heat regeneration
- Energy minimum: ~1,300 kg/h (0.98 MJ/kg total)
- Subsequent increase above 3,250 kg/h: Friction losses in heat exchangers

### Energy Consumption in Artisanal Methods

All electric; typical values per kilogram:
- **HM**: 1.15 MJ/kg (most efficient)
- **FI**: 1.28 MJ/kg (+11% vs HM)
- **DM**: 1.78 MJ/kg (+55% vs HM, due to more powerful freezing/hardening equipment)

### Comparative Perspective

Literature reports:
- **With raw materials**: 1.90 - 3.70 MJ/kg
- **Manufacturing only**: 0.70 MJ/kg
- **Our MP results**: 0.72 MJ/kg ✓ Consistent

---

## Case Study: Annual Ice Cream Demand in United Kingdom

### Context

- **UK annual demand (2018)**: 328 million liters
- **Required production**: 86,500 kg/h (industrial operation 5 days/week, 2 shifts)

### Number of Facilities Required

| Model | Facilities | Workers | Unit Cost | Annual Profit |
|---|---|---|---|---|
| **HM** | 49,744 | 49,744 | 7.59 $/kg | 21.9 k$ / facility |
| **FI** | 19,630 | 19,630 | 8.17 $/kg | 50.2 k$ / facility |
| **DM (low)** | 3,676 | 12,456 | 7.49 $/kg | 298.1 k$ / facility |
| **DM (high)** | 3,676 | 20,760 | 8.54 $/kg | 231.7 k$ / facility |
| **SP** | 1 | 1,200+ | 3.13 $/kg | 1.3 G $ (plant) |
| **MP (26 plants)** | 26 | 31,200+ | 3.60 $/kg | 47.7 M $ / plant |

### Case Study Conclusions

1. **Industrial profitability**: A single plant (SP) is most economical but requires 1,200+ employees
2. **Decentralized MP model**: 26 distributed plants achieve:
   - Costs only 15% higher than SP
   - 27% lower energy (0.72 vs 0.98 MJ/kg)
   - 32% lower carbon footprint
   - Locally sustainable business models

3. **Artisanal models**: Do not compete on price but offer:
   - Low barriers to entry
   - Sufficient income to attract entrepreneurs
   - Local job creation potential

---

## Sensitivity Analysis: Effect of Uncertainties

The model incorporates uncertainty in:

- **Raw material prices**: ±15%
- **Energy prices**: ±20%
- **Labor costs**: ±10%
- **Equipment performance**: ±5%

The shaded areas in cost graphs represent the **confidence range** derived from these uncertainties. This analysis is critical for real investment decisions.

---

## Practical Implications for Process Engineers

### 1. Production Scale Selection

- Quantifies the specific break-even point where viability changes
- Enables informed decisions in investment planning
- Identifies opportunity windows for different business models

### 2. Equipment Design

- Different scales require completely different equipment
- Equipment choice determines energy efficiency
- Strategy: maximize utilization (operate near nominal capacity)

### 3. Sustainability Considerations

- Decentralization does NOT automatically imply sustainability (see DM vs HM)
- Sustainability requires **conscious process design**
- Complete life cycle analysis (including transport) is critical for frozen products

---

## Bibliographic Reference

Almena, A., Fryer, P.J., Bakalis, S., Lopez-Quiroga, E. (2020). "Local and decentralised scenarios for ice-cream manufacture: A model-based assessment at different production scales". *Journal of Food Engineering*, 286, 110099.

https://doi.org/10.1016/j.jfoodeng.2020.110099

---

## Proposed Exercises

1. **Thermophysical Properties Calculation**: Given an ice cream with 35% fat, 5% protein, 25% carbohydrates and 35% water, calculate:
   - Initial freezing point
   - Ice fraction at -6°C
   - Apparent density

2. **Scale Analysis**: If a small artisanal ice cream maker (HM) currently produces 1 kg/h of premium ice cream and wants to double production:
   - What changes in unit cost would you expect?
   - Could it shift business models (HM → FI)?

3. **Energy Optimization**: An industrial manufacturer operates at 2,000 kg/h. According to the model:
   - What is its expected energy consumption?
   - What improvements (continuous freezing vs batch) would have the greatest impact?

4. **Regional Case Study**: Adapt the UK case analysis to your country:
   - What is annual ice cream demand?
   - How many MP plants would be needed?
   - Which model (HM/FI/DM/SP/MP) is most locally sustainable?

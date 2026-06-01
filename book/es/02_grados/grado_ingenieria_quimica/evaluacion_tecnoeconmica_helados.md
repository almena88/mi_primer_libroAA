# Evaluación Tecnoeconómica de la Fabricación de Helados a Diferentes Escalas de Producción

## Introducción

La sostenibilidad se ha convertido en un factor crítico en el diseño de sistemas de manufactura alimentaria. En particular, la industria del helado combina características que la hacen ideal para estudiar la viabilidad de diferentes paradigmas de producción:

1. **Complejidad del producto**: es un producto congelado multifásico (emulsión agua-aceite con cristales de hielo)
2. **Rango amplio de escalas**: desde fabricación casera hasta plantas industriales de gran capacidad
3. **Relevancia comercial**: coexisten modelos de negocio artesanales e industriales en el mismo mercado
4. **Intensidad energética**: consume 11-14% de la energía total en un análisis de cuna a tumba (cradle to grave)

En este capítulo, exploraremos cómo los **modelos basados en ingeniería de procesos** pueden ayudarnos a comparar la viabilidad económica y ambiental de diferentes escenarios de producción de helados, desde la fabricación casera hasta plantas industriales.

---

## Objetivos de Aprendizaje

Al finalizar este capítulo, serás capaz de:

- Comprender los **balances de masa y energía** en la producción de helados a diferentes escalas
- Evaluar la **viabilidad económica** de distintos modelos de negocio alimentario
- Estimar el **consumo energético y huella de carbono** de procesos alimentarios
- Aplicar **análisis de sensibilidad** ante incertidumbres en materias primas y energía
- Identificar los **puntos de ruptura de escala** donde un modelo de negocio se vuelve rentable

---

## Escenarios de Fabricación Analizados

El estudio presenta cinco escenarios diferentes de producción, clasificados según su grado de descentralización y escala de producción:

```{figure} evaluacion_tecnoeconmica_helados_images/page4_img1.jpeg
---
width: 90%
align: center
name: fig-ice-cream-flowsheet
---
Diagrama de flujo de una planta de fabricación de helados mostrando todos los pasos del proceso industrial. Se muestran ambas alternativas de pasteurización: batch y continua.
```

### Producción Industrial

#### Planta Única (Single Plant - SP)

- **Escala**: 650 - 3.325 kg/h
- **Operación**: 5 días/semana, 2 turnos
- **Características**: Alta especialización, economías de escala significativas
- **Tipo de pasteurización**: 
  - Batch: $T_{\text{past}} = 69.4°C$, $t > 30$ min (producción < 600 l/h)
  - Continua: $T_{\text{past}} = 79.4°C$, $t > 15$ s (con regeneración de calor)

#### Múltiples Plantas (Multi-Plant - MP)

- **Escala**: > 3.325 kg/h total (distribuido en plantas de ~3.330 kg/h cada una)
- **Ventaja clave**: Reducción de costos de transporte y almacenamiento mediante descentralización

### Producción Artesanal

#### Fabricación Casera (Home Manufacturing - HM)

- **Escala**: < 3 kg/h por instalación
- **Operación**: 5 días/semana, 1 turno (modelo gig-economy)
- **Equipos**: Equipamiento de cocina doméstica
- **Viabilidad**: Rentable por debajo de 45 kg/h producción total

#### Incubadora de Alimentos (Food Incubator - FI)

- **Escala**: ~8.7 kg/h por instalación
- **Modelo**: Equipamientos especializados compartidos por trabajadores autónomos
- **Ventaja**: Eliminación de inversión en equipamiento (solo capital de trabajo)
- **Viabilidad**: Rentable entre 45 - 650 kg/h

#### Fabricación Distribuida (Distributed Manufacturing - DM)

- **Escala**: ~21.8 kg/h por instalación (equipos modulares)
- **Modelo**: Pequeñas instalaciones tipo catering distribuidas geográficamente
- **Gestión**: Dos variantes - bajo nivel (franchising) y alto nivel (corporativa)
- **Viabilidad**: Rentable entre 650 - 3.325 kg/h

### Descripción Detallada de Procesos Artesanales

Los procesos artesanales (HM, FI, DM) reducen drásticamente la complejidad de operaciones unitarias en comparación con plantas industriales, adaptando la tecnología a capacidades domésticas o semi-industriales.

```{figure} evaluacion_tecnoeconmica_helados_images/page6_img1.jpeg
---
width: 100%
align: center
name: fig-artisanal-flowsheets
---
Artisanal manufacture flow chart for (a) Distributed Manufacturing (DM) and (b) Food Incubator (FI) and Home Manufacturing (HM). The industrial unit operations were down-scaled as domestic kitchen batch processes.
```

#### Características Operacionales de Métodos Artesanales

**Home Manufacturing (HM)**: Utiliza equipamiento de cocina doméstica modificado. El flujo de proceso incluye:
- **Mezcla**: Recipientes estándar (5-10 l) con agitación manual o batidora doméstica
- **Pasteurización**: Baño de agua térmica a temperatura controlada (~69°C, 30 min) o pasteurizador doméstico
- **Homogeneización**: Licuadora doméstica de alta velocidad (emulsificación mecánica)
- **Enfriamiento**: Refrigerador doméstico (4-8 horas) o túnel de enfriamiento casero con hielo
- **Congelación**: Máquina de helado tipo Carpigiani doméstica (~2-3 l/batch, tiempo 20-40 min)
- **Endurecimiento**: Congelador doméstico (-18°C, 2-4 horas)

**Food Incubator (FI)**: Equipamiento especializado pero compartido entre trabajadores. Mejoras respecto a HM:
- Pasteurizador de laboratorio (10-20 l, control preciso T/t)
- Homogeneizador de laboratorio (mayor eficiencia emulsificadora)
- Máquina de helado semicomercial (5-10 l/h, control de sobreaireación)
- Túnel de enfriamiento dedicado (reducción tiempo a 1-2 horas)
- Ahorros por economías de escala en insumos compartidos

**Distributed Manufacturing (DM)**: Equipamiento modular transferible entre ubicaciones. Característica distintiva:
- Sistema de congelación continua (mayor rendimiento, 15-25 kg/h)
- Hardening tunnel automatizado
- Reducción de tiempo total de proceso (6-10 horas vs 12-20 en HM/FI)
- Mayor consistencia batch-to-batch mediante sensores de control

---

## Formulaciones de Helado Estudiadas

### Helado Estándar

Composición típica de un helado industrial estándar (sabores vainilla y chocolate):

| Ingrediente | Fracción Másica | Función |
|---|---|---|
| Aceite de coco | 0.150 | Grasa base |
| Leche desnatada en polvo | 0.120 | Sólidos lácteos |
| Azúcar | 0.100 | Edulcorante principal |
| Jarabe de glucosa | 0.030 | Edulcorante secundario |
| Guar gum | 0.002 | Estabilizante |
| Carragenina | 0.001 | Estabilizante |
| Monoglicéridos | 0.002 | Emulsionante |
| Agua | 0.545 | Solvente |
| Cacao en polvo (chocolate) | 0.030 | Saborizante |

**Parámetros clave**:
- Sobreaireación (overrun): 110%
- Composición final: Grasa 7%, Proteína 0.6%, Carbohidratos 36%, Agua 60.3%

### Helado Premium

Ingredientes de mayor calidad (sabor a plátano con trozos de chocolate y nueces):

| Ingrediente | Fracción Másica |
|---|---|
| Crema (40% grasa) | 0.250 |
| Leche condensada desnatada | 0.272 |
| Azúcar | 0.100 |
| Melaza | 0.060 |
| Yema de huevo en polvo | 0.010 |
| Lecitina de soja | 0.002 |
| Puré de plátano | 0.075 |
| Trozos de chocolate | 0.085 |
| Nueces | 0.055 |

**Parámetros clave**:
- Sobreaireación: 27%
- Composición final: Grasa 42.9%, Proteína 7.1%, Carbohidratos 47.6%, Agua 2.4%

---

## Modelado Matemático de Propiedades Termofísicas

Para cada formulación, calculamos las propiedades que varían con la temperatura mediante reglas de mezcla basadas en los componentes principales.

### Punto de Congelación Inicial (TIF)

$$T_{\text{IF}} = 9.4915 \times 10^{-5} \left( \sum \frac{x_k M_{\text{sacarosa}}}{M_k} \cdot 100 \right)^2 + 6.1231 \times 10^{-2} \left( \sum \frac{x_k M_{\text{sacarosa}}}{M_k} \cdot 100 \right) + \frac{x_{\text{MSNF}} \times (-2.37)}{x_w}$$

donde:
- $x_k$: fracción másica del componente $k$
- $x_w$: fracción másica de agua
- $x_{\text{MSNF}}$: fracción de sólidos no grasos lácteos

### Fracción de Hielo

$$x_{\text{ice}}(T) = x_w \left( 1 - \frac{T_{\text{IF}}}{T} \right)$$

### Calor Específico

$$c_p = \sum_j x_j c_{p,j} - L_f\left(T_{\text{IF}}\right) \frac{dx_{\text{ice}}}{dT}$$

donde $L_f = 333.8 + 2.1165 \cdot T$ es el calor latente de fusión en kJ/kg.

### Sobreaireación (Overrun)

$$Ov_{\text{ic}} = \frac{V_{\text{aerated}} - V_{\text{non-aerated}}}{V_{\text{non-aerated}}} \times 100\%$$

La sobreaireación incrementa el volumen total incorporando aire en forma de pequeñas burbujas. Es crítica para la textura y el volumen final de venta.

---

## Análisis de Costos Unitarios

Uno de los resultados clave del estudio es cómo varían los costos unitarios ($/kg) según la escala de producción:

```{figure} evaluacion_tecnoeconmica_helados_images/page8_img1.jpeg
---
width: 100%
align: center
name: fig-unit-costs
---
Variación del costo unitario ($/kg) para diferentes escalas de fabricación: (a) helado premium vendido en envases de 500 ml, (b) helado premium vendido en envases de 150 ml y (c) helado estándar vendido en envases de 1000 ml. Las áreas sombreadas representan la región de confianza establecida por las incertidumbres.
```

### Regiones de Viabilidad

Las curvas de costo pueden dividirse en tres regiones:

1. **Región No Viable**: Costos muy altos a bajas capacidades; pendiente pronunciada
2. **Región de Transición**: Economías de escala visibles; reducción significativa de costos
3. **Región de Meseta**: Aumentos adicionales de capacidad no mejoran costos unitarios (saturación de equipamiento)

### Hallazgos Clave

- **HM es rentable** por debajo de 45 kg/h (costo < precio de mercado)
- **DM con gestión baja** es más competitivo que HM/FI en producciones intermedias (100-1.000 kg/h)
- **SP requiere mínimo 650 kg/h** para ser rentable
- **Plantas múltiples** mejoran márgenes a producciones > 3.325 kg/h

---

## Análisis de Consumo Energético

El consumo energético es un factor crítico para la sostenibilidad del proceso.

```{figure} evaluacion_tecnoeconmica_helados_images/page9_img1.jpeg
---
width: 100%
align: center
name: fig-energy-consumption
---
(a) Consumo de energía en un escenario de planta única (SP). Aparece una discontinuidad (señalada con una flecha) cuando el proceso cambia de pasteurización batch a continua, lo que permite la regeneración de calor. (b) Consumo de energía para HM, FI y DM. Las restricciones de números enteros del equipamiento de procesamiento causan discontinuidades en la gráfica de energía. El consumo mínimo se logra operando a capacidad máxima.
```

### Consumo en Plantas Industriales

Para una planta única (SP):

$$E_{\text{total}} = E_{\text{calor}} + E_{\text{enfriamiento}} + E_{\text{congelación}} + E_{\text{bombeo}}$$

**Valores típicos**:
- Cambio batch → continua (600 l/h): Ahorro de ~15% mediante regeneración de calor
- Mínimo energético: ~1.300 kg/h (0.98 MJ/kg total)
- Aumento posterior a 3.250 kg/h: Pérdidas por fricción en intercambiadores

### Consumo en Métodos Artesanales

Todos eléctricos; valores típicos por kilogramo:
- **HM**: 1.15 MJ/kg (más eficiente)
- **FI**: 1.28 MJ/kg (+11% vs HM)
- **DM**: 1.78 MJ/kg (+55% vs HM, equipos de congelación/hardening más potentes)

### Perspectiva Comparativa

La literatura reporta:
- **Con materias primas**: 1.90 - 3.70 MJ/kg
- **Solo manufactura**: 0.70 MJ/kg
- **Nuestros resultados MP**: 0.72 MJ/kg ✓ Coherente

---

## Caso de Estudio: Demanda Anual de Helado en Reino Unido

### Contexto

- **Demanda anual UK (2018)**: 328 millones de litros
- **Producción requerida**: 86.500 kg/h (operación industrial 5 días/semana, 2 turnos)

### Número de Instalaciones Necesarias

| Modelo | Instalaciones | Trabajadores | Costo Unitario | Ganancia Anual |
|---|---|---|---|---|
| **HM** | 49.744 | 49.744 | 7.59 $/kg | 21.9 k$ / instalación |
| **FI** | 19.630 | 19.630 | 8.17 $/kg | 50.2 k$ / instalación |
| **DM (bajo)** | 3.676 | 12.456 | 7.49 $/kg | 298.1 k$ / instalación |
| **DM (alto)** | 3.676 | 20.760 | 8.54 $/kg | 231.7 k$ / instalación |
| **SP** | 1 | 1.200+ | 3.13 $/kg | 1.3 G $ (planta) |
| **MP (26 plantas)** | 26 | 31.200+ | 3.60 $/kg | 47.7 M $ / planta |

### Conclusiones del Caso de Estudio

1. **Rentabilidad industrial**: Una planta única (SP) es la más económica pero requiere 1.200+ empleados
2. **Modelo descentralizado MP**: 26 plantas distribuidas logran:
   - Costos solo 15% superiores a SP
   - Energía 27% inferior (0.72 vs 0.98 MJ/kg)
   - Huella de carbono 32% menor
   - Modelos de negocio sostenibles localmente

3. **Modelos artesanales**: No compiten en precio pero ofrecen:
   - Barreras de entrada bajas
   - Ingresos suficientes para atraer emprendedores
   - Potencial de creación de empleo local

---

## Análisis de Sensibilidad: Efecto de Incertidumbres

El modelo incorpora incertidumbre en:

- **Precios de materias primas**: ±15%
- **Precios de energía**: ±20%
- **Costos laborales**: ±10%
- **Rendimiento de equipamiento**: ±5%

Las áreas sombreadas en las gráficas de costos representan el **rango de confianza** derivado de estas incertidumbres. Este análisis es crítico para decisiones de inversión reales.

---

## Implicaciones Prácticas para Ingenieros de Procesos

### 1. Selección de Escala de Producción

- Cuantifica el punto de ruptura específico donde cambia la viabilidad
- Permite decisiones informadas en planificación de inversión
- Identifica ventanas de oportunidad para diferentes modelos de negocio

### 2. Diseño de Equipamiento

- Diferentes escalas requieren equipamiento completamente distinto
- La elección de equipos determina eficiencia energética
- Estrategia: maximizar utilización (operar cerca de capacidad nominal)

### 3. Consideraciones de Sostenibilidad

- La descentralización **NO implica automáticamente sostenibilidad** (ver DM vs HM)
- La sostenibilidad requiere **diseño consciente de procesos**
- El análisis de ciclo de vida completo (incluyendo transporte) es crítico para helados congelados

---

## Referencia Bibliográfica

Almena, A., Fryer, P.J., Bakalis, S., Lopez-Quiroga, E. (2020). "Local and decentralised scenarios for ice-cream manufacture: A model-based assessment at different production scales". *Journal of Food Engineering*, 286, 110099.

https://doi.org/10.1016/j.jfoodeng.2020.110099

---

## Ejercicios Propuestos

1. **Cálculo de propiedades termofísicas**: Dado un helado con 35% grasa, 5% proteína, 25% carbohidratos y 35% agua, calcula:
   - Punto de congelación inicial
   - Fracción de hielo a -6°C
   - Densidad aparente

2. **Análisis de escala**: Si una pequeña heladería artesanal (HM) produce actualmente 1 kg/h de helado premium y quiere duplicar su producción:
   - ¿Qué cambios en costo unitario esperarías?
   - ¿Podría cambiar su modelo de negocio (HM → FI)?

3. **Optimización energética**: Un fabricante industrial opera a 2.000 kg/h. Según el modelo:
   - ¿Cuál es su consumo energético esperado?
   - ¿Qué mejoras (congelación continua vs batch) tendrían mayor impacto?

4. **Estudio de caso regional**: Adapta el análisis del caso UK a tu país:
   - ¿Cuál es la demanda anual de helado?
   - ¿Cuántas plantas MP serían necesarias?
   - ¿Qué modelo (HM/FI/DM/SP/MP) es más sostenible localmente?

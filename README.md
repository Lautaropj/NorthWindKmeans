# 📊 Clustering de Clientes con KMeans — Northwind

Este proyecto implementa un modelo de **segmentación de clientes** utilizando **KMeans**, basado en datos de la base **Northwind**.  
El objetivo es identificar grupos de clientes según su comportamiento de compra.

---

## 🚀 Características del modelo

El código implementa:

- Extracción de datos desde SQL Server (Customers, Orders y Order Details)
- Cálculo de métricas por cliente:
  - Total de órdenes
  - Total gastado (incluye descuento)
  - Promedio gastado por orden
- Estandarización de variables con **StandardScaler**
- Selección del número óptimo de clusters usando el **método del codo**
- Entrenamiento del modelo KMeans
- Detección y exclusión de outliers (percentil 0.99)
- PCA para visualización en 2D
- Gráficos de clusters (con outliers y sin outliers)
- Exportación de resultados a CSV

---

## 🗄️ Consulta SQL utilizada

```sql
SELECT 
    c.CustomerID,
    COUNT(o.OrderID) AS TotalOrdenes,
    ROUND(SUM(od.Quantity * od.UnitPrice * (1 - od.Discount)), 2) AS TotalGastado,
    ROUND(AVG(od.Quantity * od.UnitPrice * (1 - od.Discount)), 2) AS PromedioOrden
FROM Customers c
LEFT JOIN Orders o ON c.CustomerID = o.CustomerID
LEFT JOIN [Order Details] od ON o.OrderID = od.OrderID
GROUP BY c.CustomerID
HAVING COUNT(o.OrderID) > 0
ORDER BY TotalGastado DESC;
```

---

## 🧮 Flujo del modelo

### 1️⃣ Cargar datos
Usa `pandas.read_sql_query()` y una función personalizada `obtener_conexion()`.

### 2️⃣ Escalar variables
```python
scaler = StandardScaler()
X = scaler.fit_transform(df[['TotalOrdenes', 'TotalGastado', 'PromedioOrden']])
```

### 3️⃣ Método del codo
Genera una gráfica para evaluar el mejor valor de **k**.

### 4️⃣ Entrenar KMeans inicial
```python
kmeans = KMeans(n_clusters=3, random_state=42)
df['cluster'] = kmeans.fit_predict(X)
```

### 5️⃣ Detección de outliers (percentil 0.99)
```python
umbral = df['TotalGastado'].quantile(0.99)
df_model = df[df['TotalGastado'] <= umbral]
```

### 6️⃣ Nuevo clustering sin outliers
Se reentrena KMeans y se aplica PCA para mejor visualización.

---

## 📈 Visualizaciones generadas

- Método del codo
- Clusters iniciales (con outliers)
- PCA clusters sin outliers
- Gráfico Cantidad de Órdenes vs Total Gastado (sin outliers)

---

## 💾 Archivos exportados

El script genera:

- `clientes_clusters_inicial.csv`  
- `clientes_clusters_sin_outliers.csv`

Ambos en formato `;` para compatibilidad con Excel.

---

## 🔧 Requisitos

Instalar dependencias:

```
pip install pandas numpy matplotlib seaborn scikit-learn pyodbc
```

---

## 🔗 Conexión a SQL Server

El archivo **connect.py** debe incluir:

```python
import pyodbc

def obtener_conexion():
    return pyodbc.connect(
        "Driver={ODBC Driver 17 for SQL Server};"
        "Server=localhost;"
        "Database=Northwind;"
        "Trusted_Connection=yes;"
    )
```

---

## 🎯 Objetivo del proyecto

Proveer un ejemplo simple, claro y automatizable de un pipeline de **ML aplicado a negocio**, generando una segmentación útil para:

- Marketing
- Fidelización
- Análisis de comportamiento del cliente
- Descubrimiento de patrones de compra

---

## 📬 Contacto

Para mejoras, dashboards o versionar este modelo con más features, ¡podés escribirme!


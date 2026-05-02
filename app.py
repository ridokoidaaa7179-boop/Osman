import streamlit as st
import pandas as pd

# إعدادات واجهة ورشة خط
st.set_page_config(page_title="نظام ورشة خط الذكي", layout="wide")
st.title("🛠️ لوحة تحكم ورشة خط - الإدارة المالية والتسويق")

# رابط الجدول الخاص بك
sheet_url = "https://docs.google.com/spreadsheets/d/1-GxATyboftW38Vwp8xB7BDjzKaZbKXbNve_ZIJdXvWs/gviz/tq?tqx=out:csv"

# حسابات المستهدف (50 ألف ريال)
target = 50000
try:
    df = pd.read_csv(sheet_url)
    df['سعر البيع'] = pd.to_numeric(df['سعر البيع'], errors='coerce').fillna(0)
    current_sales = df['سعر البيع'].sum()
except:
    current_sales = 0

# عرض المؤشرات المالية
col1, col2 = st.columns(2)
with col1:
    st.metric("المبيعات الحالية", f"{current_sales:,.0f} ريال")
with col2:
    remaining = max(target - current_sales, 0)
    st.metric("المتبقي للهدف", f"{remaining:,.0f} ريال")

st.progress(min(current_sales / target, 1.0))

st.divider()

# قسم التسويق الآلي
st.header("🚀 مساعد التسويق الذكي")
uploaded_file = st.file_uploader("ارفع صورة المنتج للإعلان عنه", type=['jpg', 'png'])
if uploaded_file:
    st.image(uploaded_file, width=300)
    st.success("💡 مقترح إعلاني: 'تميز مع أعمال الليزر من ورشة خط. دقة، فخامة، وسرعة في التنفيذ. اطلب تصميمك الآن!'")

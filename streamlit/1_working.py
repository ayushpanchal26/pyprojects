import streamlit as st
st.title("Streamlit text and display example")
st.header("This is a Header")
st.subheader("This is subheader")
st.subheader("Ayush Panchal")
st.text("This is text data ")
st.write("This is default font ")

# markdown
st.markdown("This is markdown")
st.markdown("# This is markdown heading")
st.markdown("## this is markdown subheading")
st.markdown("### this **subsheading**")
st.markdown("[Markdown cheat](https://www.youtube.com/watch?v=hff2tHUzxJM&list=PLc2rvfiptPSSpZ99EnJbH5LjTJ_nOoSWW)")

st.markdown("""
1. First Item
2. Second Item
3. Third Item

- First item
- Second item
- Third item
            
` here is a code for searchig algos
            
    def bubble(arr,n):
    print("Befor bubble sort")
    print(f"{arr}")

    for i in range(n,-1,-1):
        for j in range(0,i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1] , arr[j]
                didswap = 1
    print("After bubble sort")
    return arr`
""")

st.markdown("### HTML")
html = """
<h1 style="color:orange;"> A blue Heading</h1>
<p style="color:aqua;">A red paragraph.</p>
"""
st.markdown(html,unsafe_allow_html=True)
st.markdown("---")
st.markdown("## Latex CODE")
st.divider()
st.latex("x^2 + y^2 = z^2")
st.latex("y = \sqrt{x^2+1}")
st.latex("y = mx+c")
st.latex(r"g(x) = \frac{1}+{x^2 + y^3}")
st.markdown("### Ayush Panchal")
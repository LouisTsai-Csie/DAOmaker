import streamlit as st

def app():
    st.header('DAO 討論與投票區')
    tab1, tab2 = st.tabs(["現有提案", "討論區"])
    
    with tab1:
        st.text('提案數量: 3')
        with st.expander('新增鏈選擇'):
            st.write('提案摘要：目前支援的鏈種比較少，希望可以增加更多的選擇，目前的想法有以下幾種：\n包括 flow, tezos, sol\n以下是詳細的提案內容介紹...')
        with st.expander('安全性考量'):
            st.write('日前 SOLANA 鏈上的錢包 Slope 遭受駭客入侵，受到慘重的損失，希望針對該部分可以進行深入研究並做為借鏡，以下為詳細提案內容...')
        with st.expander('投票方式決定'):
            st.write('對於現有的投票與提案方式，是否有更佳的方式可以增進表決速度或公平性，例如引入平方投票法等等\n以下提出一些建議作為拋磚引玉，歡迎大家討論')
        st.button('新增提案')

    with tab2:
        pass
        

import os
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
"""
Streamlit Currency Converter Interface
======================================

This module provides an interactive web interface for the currency converter
using Streamlit. It fetches live rates and displays visual conversion metrics.
"""

import streamlit as st
from constants import CURRENCIES
from currency_convertor import get_exchange_rate, convert_currency


def main() -> None:
    """
    Main function to construct and execute the Streamlit application.
    """
    st.title(":dollar: Currency Converter")
    st.markdown(
        "This tool allows you to convert between different currencies 🌎. "
        "Simply select the source and target currencies, enter the amount "
        "you wish to convert, and click the **Convert** button to see the result."
    )

    # Input fields
    base_currency = st.selectbox("Select the base currency", CURRENCIES, index=0)
    target_currency = st.selectbox("Select the target currency", CURRENCIES, index=26)

    amount = st.number_input(
        label="Enter the amount to convert", 
        min_value=0.0, 
        value=100.0, 
        step=1.0
    )

    if st.button("Convert"):
        with st.spinner("Fetching live exchange rates..."):
            exchange_rate = get_exchange_rate(base_currency, target_currency)
        
        if exchange_rate is not None:
            converted_amount = convert_currency(amount, exchange_rate)
            st.success(f"✅ {amount} {base_currency} is equal to {converted_amount:.2f} {target_currency}")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Base Currency", value=f"{amount:.2f} {base_currency}")
                
            with col2:
                st.markdown(
                    "<h1 style='text-align: center; margin: 0; color: green;'>&#8594;</h1>", 
                    unsafe_allow_html=True
                )
                
            with col3:
                st.metric("Target Currency", value=f"{converted_amount:.2f} {target_currency}")
        else:
            st.error("Failed to retrieve exchange rate. Please check your connection or try again later.")

    st.markdown("---")
    st.markdown("### About This tool")


if __name__ == "__main__":
    main()
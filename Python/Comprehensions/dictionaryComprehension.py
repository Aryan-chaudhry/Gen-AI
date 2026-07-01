tea_prices_inINR = {
    "Masala Chai " : 40,
    "green chai" : 50
}

tea_prices_inUSD = {tea:price/80 for tea, price in tea_prices_inINR.items()}

print(tea_prices_inUSD)
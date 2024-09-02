****Monthly checking account fee @ Hometown Bank

start
    INPUT   accountBalance
    INPUT   countoverDrawn

    balance = accountBalance
    fee = -5
    overDrawnFee = (balance *.01) + fee
    
    newbalance = balance - overDrawnFee

    PRINT overDrawnFee
    PRINT newbalance
    PRINT "Thanks for using this program"
end

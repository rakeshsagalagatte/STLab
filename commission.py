def isvalid(locks , stock , barrel):
    if locks in range(1,71) and stock in range(1,81) and barrel in range(1,91):
        return True
    return False

lock_price,stock_price,barrel_price = [45, 30 , 25]
total_lock,total_stock,total_barrel= [0,0,0]
while True:
    try:
        lock,stock,barrel = map(int , input('Enter the total number of locks, stocks, barrel : ').split())
    except:
        print('Invalid inputs')
    if lock == -1:
        break
    total_lock += lock
    total_stock += stock
    total_barrel += barrel
    if isvalid(total_lock , total_stock , total_barrel) == False:
        print('Inputs out of bounds , Re-enter the values')
        total_lock -= lock
        total_stock -= stock
        total_barrel -= barrel

sales = total_lock * lock_price + total_stock * stock_price + total_barrel * barrel_price

if sales <= 1000:
    commission =  0.1 * sales
elif sales > 1000 and sales <= 1800:
    commission = 0.15 *  sales
else :
    commission = 0.2 * sales

print('Total sales = ' + str(sales))
print('Total commission : ' + str(commission))

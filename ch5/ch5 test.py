def main():
    tic_a=int(input('how many tiket sold in class A?'))
    tic_b=int(input('how many tiket sold in class B?'))
    tic_c=int(input('how many tiket sold in class C?'))

    income=income_seat_sale(tic_a,tic_b,tic_c)

    print ('the amont income from ticket sales is $:', income)

def income_seat_sale(tic_a,tic_b,tic_c):
    income=(tic_a*20)+ (tic_b*15)+ (tic_c*10)
    return income
main()
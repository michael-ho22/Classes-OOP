import PatientClass as Pat
import ProcedureClass as Pro



def main():

    patients = [Pat.Patient('1', 'Matt Jones', '123 Main st, Waco TX 76706', '254-555-7415', 'TRUE')]


    procedures = [
        Pro.Procedure('Physical Exam', '2/15/2022', 'Dr.Irvine', 250, '1'),
        Pro.Procedure('MRI', '2/15/2022', 'Dr.Hamilton', 1500, '1'),
        Pro.Procedure('CT Scan', '2/17/2022', 'Dr.Drey', 1200, '2')
    ]

    print('*** Patient Bill ***')
    for info in patients:
        total_charge = 0
        print('Name:', info.get_name())
        print('Address:', info.get_address())
        print('Phone:', info.get_phone(), '\n')

        for procedure in procedures:
            if procedure.get_ID() == info.get_ID():
                total_charge +=  procedure.get_charges()
                print('Procedure:', procedure.get_name())
                print('Date:', procedure.get_pro_date())
                print('Practitioner:', procedure.get_practitioner())
                print('Charge: $', format(procedure.get_charges(), ',.2f'), '\n')

        if info.get_veteran_status() == 'TRUE':
            total_charge *= 0.6

        print('Total Charges: $', format(total_charge, ',.2f'))


        
main()
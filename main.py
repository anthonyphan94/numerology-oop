from person import Person
from datetime import date

print("Today:", date.today())
person_1 = Person('Anthony Bao Quoc Phan', '04101994')

# Thieu chi so can bang, Thieu chi so nhan cach
name = person_1.name
print('Ho Ten', person_1.name)
print('Ngay sinh:', person_1.dob)
print('Chi so duong doi:', person_1.tinh_chi_so_duong_doi())
print('Chi so su menh:', person_1.tinh_chi_so_su_menh())
print('Chi so truong thanh:', person_1.tinh_chi_so_truong_thanh())
print('Chi so can bang:', person_1.tinh_chi_so_can_bang())
print('Chi so ngay sinh:', person_1.tinh_chi_so_ngay_sinh())
print('Chi so lk duong doi su menh:', person_1.tinh_chi_so_lk_duong_doi_su_menh())
print('Chi so linh hon:', person_1.tinh_chi_so_linh_hon())
print('Chi so nhan cach:', person_1.tinh_chi_so_nhan_cach())
print('Chi so thieu:', person_1.tinh_chi_so_thieu())
print('Chi so tiem thuc:', person_1.tinh_chi_so_tiem_thuc())
print('Chi so dam me:', person_1.tinh_chi_so_dam_me())
#
print('Chi so tu duy ly tri:', person_1.tinh_chi_so_tu_duy_ly_tri())
print('Chi so chang:', person_1.tinh_chi_so_chang())
print('Chi So thach thuc: ', person_1.tinh_chi_so_thach_thuc())
print('Chi so nam: ', person_1.tinh_chi_so_nam())
print('Chi so thang:', person_1.tinh_chi_so_thang())
print('Chi so ngay:',person_1.tinh_chi_so_ngay())

from calculation import simplify, this_year, this_date, this_month
from name_dictionary import my_dict, calculate_total_character, tinh_chu_cai_dau_tien, tinh_vowel, full_name, \
    tinh_consonant, check_in_list, get_max_count


class Person:

    def __init__(self, name, dob):
        self.name = name
        self.dob = dob
        self.month = dob[0:2]
        self.date = dob[2:4]
        self.year = dob[4:len(dob)]
        self.chi_so_su_menh = None
        self.chi_so_duong_doi = None
        self.chi_so_truong_thanh = None
        self.chi_so_can_bang = None
        self.chi_so_ngay_sinh = None

    def set_name(self, name):
        self.name = str(name)

    def set_dob(self, age):
        self.dob = str(age)

    def simplify_date(self):
        return simplify(int(self.date))

    def simplify_month(self):
        return simplify(int(self.month))

    def simplify_year(self):
        return simplify(int(self.year))

    def tinh_chi_so_duong_doi(self):
        self.chi_so_duong_doi = simplify(
            int((simplify(self.date))) + int((simplify(self.month))) + int((simplify(self.year))))

        return self.chi_so_duong_doi

    def tinh_chi_so_su_menh(self):
        self.chi_so_su_menh = calculate_total_character(self.name, full_name)
        return self.chi_so_su_menh

    def tinh_chi_so_truong_thanh(self):
        self.chi_so_truong_thanh = str(simplify((int(simplify(self.tinh_chi_so_su_menh())) +
                                                 int(simplify(self.tinh_chi_so_duong_doi())))))
        return self.chi_so_truong_thanh

    def tinh_chi_so_can_bang(self):
        self.chi_so_can_bang = tinh_chu_cai_dau_tien(self.name)
        return self.chi_so_can_bang

    def tinh_chi_so_ngay_sinh(self):
        return simplify(self.date)

    def tinh_chi_so_lk_duong_doi_su_menh(self):
        return abs(int(self.chi_so_duong_doi) - int(self.chi_so_su_menh))

    def tinh_chi_so_linh_hon(self):
        return calculate_total_character(self.name, tinh_vowel)

    def tinh_chi_so_nhan_cach(self):
        return calculate_total_character(self.name, tinh_consonant)

    def tinh_chi_so_thieu(self):
        return check_in_list(self.name)

    def tinh_chi_so_tiem_thuc(self):
        chi_so_tiem_thuc = 9 - len(self.tinh_chi_so_thieu())
        return chi_so_tiem_thuc

    def tinh_chi_so_dam_me(self):
        converted_name = full_name(self.name)
        return get_max_count(converted_name)

    def tinh_chi_so_tu_duy_ly_tri(self):
        name_list = self.name.lower().split()
        first_name = name_list[0]
        int_simplified_first_name = int(simplify(full_name(first_name)))
        result = simplify(int_simplified_first_name + int(simplify(self.date)))
        return result

    def tinh_chi_so_chang(self):
        list_chang = []

        chang_1 = simplify(int(simplify(self.date)) + int(simplify(self.month)))
        chang_2 = simplify(int(simplify(self.date)) + int(simplify(self.year)))
        chang_3 = simplify(int(chang_1) + int(chang_2))
        chang_4 = simplify(int(simplify(self.month)) + int(simplify(self.year)))

        return [chang_1, chang_2, chang_3, chang_4]

    def tinh_chi_so_thach_thuc(self):
        thach_thuc_1 = abs(int(simplify(self.date)) - int(simplify(self.month)))
        thach_thuc_2 = abs(int(simplify(self.date)) - int(simplify(self.year)))
        thach_thuc_3 = abs(int(thach_thuc_1) - int(thach_thuc_2))
        thach_thuc_4 = abs(int(simplify(self.month)) - int(simplify(self.year)))

        return [thach_thuc_1, thach_thuc_2, thach_thuc_3, thach_thuc_4]

    def tinh_chi_so_nam(self):
        chi_so_nam = simplify(int(simplify(self.date)) + int(simplify(self.month)) + int(simplify(this_year)))

        return chi_so_nam

    def tinh_chi_so_thang(self):
        chi_so_thang = simplify(int(self.tinh_chi_so_nam()) + int(simplify(this_month)))

        return chi_so_thang

    def tinh_chi_so_ngay(self):
        chi_so_ngay = simplify(int(self.tinh_chi_so_thang()) + int(simplify(this_date)))

        return chi_so_ngay





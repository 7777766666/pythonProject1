import datetime;
from pprint import pprint
from copy import deepcopy

print("Lol", 555, "999");
print(print);
# name = input("Enter someThing: ");
# print(name )
lol = "Lol";
print(dir(lol))
x = 777;
print(dir(x));
print(lol.upper());

print(dir())
print(dir(__builtins__))
# input("Enter name, please: ");
# zzz = input("Enter name, please: ");
# ddd = input("age: ")
# aaa = input("Your cource: ")
# print(zzz + " " + ddd + " " + " " + aaa);
# print(zzz.capitalize());


def myFn():
    print("Hello");

print("Lol");

myFn();

print(datetime.MAXYEAR);
print(datetime.MINYEAR);

a = 10;
b = 3;


def myInstr(a, b):
    return a * b + 100;


f = myInstr(a, b);

print(f);

name_lol = "Lol!!!";
print(name_lol);
name_lol = "1234567890";
name_lol2 = "abcdefgh";
print(name_lol);

id(lol);

dal = lol;
print(id(lol));
print(id(dal));

pop = "Lol";
print(id(pop));
top = True;

print(type(pop));
print(type(b));
print(type(top));

ppp = "lol" \
      "lol      " \
      "555";
xxxx = """ I
        soo
all
   good
"""
print(ppp);
print(xxxx);
print(type(xxxx));
print(type(int));
print(id(xxxx))
# print(type(function));

print(len(name_lol));

print(name_lol[0]);
print(name_lol[1]);
print(name_lol[2]);
print(name_lol[3]);
print(name_lol[5 : 8]);
print(name_lol[:6]);
print(name_lol[4:]);
print(name_lol.count(name_lol));
print(name_lol2.upper());
print(name_lol2.count("bcdef"));  #содержит ли, аналог контэйн
name_new = name_lol2.replace("abc", "123");
print(name_new);
print(ppp.count("  "));  #количество данного выражения в нашей переменной 3*2  "  "
print(ppp[-2]);
print(ppp[3: -2]);
print(ppp[-2: ]);

x = "555";
x = int(x);
print(type(x));
x += 7.88888;
print(x);
print(type(x));

print(pow(2, 10));  #2 в 10 степени 1024
zz = 1_000_000;
print(zz + x);

# qqq = input("Enter num: ")
qqq = 100;
print(type(qqq));
qqq = int(qqq);
print(type(qqq));

cc = 0.2+0.3+0.4+0.5+0.6+0.1+0.7
print(cc);
print(type(cc));

bb = "444.444";
cc = float(bb);
rr =  str(bb) + " hello " + str(type(bb));
print(rr);

x = 66.66;
print(x.__round__());
print(round(x));

k = 2;
complex_x = 10 + 9j;
complex_y = 20 + 10j;

print(str( complex_y + complex_x) + " and "+ str(type(complex_y)));

print ("lll" < "z")

print([1,2,3,9] > [1,9]);
print({a: 6} == {a: 6});

ss = 2;
ee = 2.5;
print(ss+ee);
print(ee+ss);

nnn = True;
bbb = 7;
print(nnn + bbb);
print(bbb+nnn);

gg = "Lob ";
g = 10;
# print(g * gg);
# print(gg * g);

print(g.__mul__(gg));   #NotImplemented
print(gg.__mul__(g));   #Lob Lob Lob Lob Lob Lob Lob Lob Lob Lob
print(gg.__rmul__(g));  #Lob Lob Lob Lob Lob Lob Lob Lob Lob Lob
print(bool.__doc__);

my_list = [];
print("!!!")
print(my_list.__doc__);
print(help(my_list.__eq__));
print(my_list.__eq__);

list_fruits = ["apple", "banana", "lime"];
number_list_1 = [100, 300, 1000];
number_list_2 = [1000, 300, 100];
user_input_list = ["Hello", 100, True, 99.99];

print(number_list_1 == number_list_2);  #False
print(number_list_1.__len__());
print(len(number_list_2));
print(len(number_list_2) == len(number_list_1));
print(user_input_list[-2]);
print(user_input_list[3]);
print(user_input_list[2] == user_input_list[-2]);
user_input_list[-2] = False
print(user_input_list[-2]);
del user_input_list[-2];
print(user_input_list);

users = [
    {
        "id_user": 888,
        "name_user": "Ann"
    },
    {
        "id_user": 891,
        "name_user": "Tom"
    }
];



print(len(users));
print(users);
print(users[0]);
print(users[1]);

user_inputs = [True, "Lol", 33.33, 100];
ff = user_inputs.pop();
print(str(user_inputs) + " ! " + str(ff));
user_inputs.pop(-2);
print(user_inputs);
user_inputs.append("SuperLol");
print(user_inputs);
# user_inputs.sort();
# print(user_inputs);
# user_inputs.sort(reverse=True);
# print(user_inputs);
print("!!!@@@@@@@@")
num_different = [55, -99, -999, 567];
num_different.sort();
print(num_different);
print(min(num_different));
print(max(num_different));
print(sum(num_different));
print(sum(num_different)/len(num_different));
num_different2 = [10, 10];
num_different3 = num_different2 + num_different;
print(num_different3);
num_different4 = num_different2.__add__(num_different).__add__(num_different3);
print(num_different4);


# num_different.sort();
print(num_different);
num_different.sort(reverse=True);
print(num_different);
str_some = ["qwe", "abc", "aaa", "zzz", "azzz"];
str_some.sort();
print(str_some);
some_text = "Hello world for ever";
some_text_lettes = list(some_text);
print(some_text_lettes);

users2 ={ "id_user": 888,
          "name_user": "Ann" };
print(users2);
users_letters = list(users2);
print(users_letters);

num_different5 = num_different4[:3];
print(num_different5)
num_different6 = num_different4[2: -2];
print(num_different4);
print(num_different6);
num_different7 = num_different4[:];
print(num_different7);
num_different8 = num_different7;
print(id(num_different4));
print(id(num_different7));
print(id(num_different8));
num_different9 = num_different4.copy();
print(id(num_different9));
num_different10 = list(num_different4);
print(id(num_different10));
print(num_different10.count(10));
num_different10.append(888);
print(num_different10);
num_different10.insert(2, -666);
print(num_different10);
num_different10.extend("abczzz");
print(num_different10);

list_l = [6, 8];
f = {a : "Tom"};

list_rofl = [-6, True, "Lol", list_l, f];
print(list_rofl);
del list_rofl[2];
print(list_rofl);
print(len(list_rofl));
print(list_rofl.__len__());
list_rofl.reverse();
print(list_rofl);
list_rofl2 = ["mem", 99];
list_rofl +=list_rofl2;
print(list_rofl);
print(list_rofl[0:7]);

rofl = ["lol", "MegaLol"];
rofl2 = [10, -2];
rofl = rofl.__add__(rofl2);
print(rofl);
rofl +=rofl2;
print(rofl);

my_car = {
    "model": "Tesla",
    "price": 5_555,
    "engine": "volt",
    "v": 5.5,
};

another_car = {
    "engine": "volt",
    "v": 5.5,
    "model": "Tesla",
    "price": 5_555,
};
print(id(another_car));
print(id(my_car));
print(another_car == my_car);
print(another_car.__eq__(my_car));

print(my_car["price"]);
print(another_car["model"]);

my_car["price"] = 999_999;
print(my_car);
print(dir(my_car));
my_car["fast"] = True;
print(my_car);
my_car["fast"] = False;
print(my_car);
pprint(my_car);
del my_car["fast"];
print(my_car);
lol_key = "model";
my_car[lol_key] = "BMW";
print(my_car);
my_car["lol_inside" "price_in_uk"]= 65000;
my_car["lol_inside""price_in_usa"] = 55_000;
# my_car["lol_inside""different"] = True;
print(my_car);
brand = "Audi";
my_car["model"] = brand;
print(my_car);
print(len(my_car));
del my_car["lol_inside" "price_in_uk"];
del my_car["lol_inside""price_in_usa"];
print(len(my_car));
print(my_car.get("some_key"));
print(my_car.get("some_key",999));

lol_disk = {};
print(id(lol_disk));
print(type(lol_disk));
lol_disk ["price"] = 100.5;
lol_disk["type"] = "ssd";
print(lol_disk);
print(lol_disk.__doc__);
print(lol_disk.items());
print(type(lol_disk));
print(lol_disk.keys());
print(list(lol_disk.keys()));
# print(lol_disk.clear());
print(lol_disk.get("lol", 888888888888));

# my_list = [["one", "Lol"], ["two", True], ["tree", 66.66]];
my_list = [("one", "Lol"), ["two", True], ["tree", 66.66]];
my_dict = dict(my_list);
print(my_dict);

lol_lol = {};
print(type(lol_lol));

# k1 = input("Enter key1: ")
# z1 = input("Enter znachenie 1: ")
# lol_lol [k1] = z1;
# k2 = input("Enter key2: ")
# z2 = bool(input("Enter znachenie 2: "))
# lol_lol[k2] = z2;
# k3 = input("Enter key3: ")
# z3 = int(input("Enter znachenie 3: "));
# lol_lol[k3] = z3;
# print(lol_lol);
# lol_lol["4"] = float(-99.99);
# del lol_lol["1"];
# print(lol_lol);

lol_tuple1 = (1, 5, 100);
lol_tuple2 = (10.999, True, False, "Lol");
print(type(lol_tuple2));
lol_tuple3 = (100, 1, 5);
lol_tuple4 = (100, 1, 5);
print(lol_tuple3.__eq__(lol_tuple1));
print(lol_tuple4 == lol_tuple3);
print(len(lol_tuple4));
print(lol_tuple4[-2]);
print(lol_tuple2.__len__());
users10 = (
    {
        "id": 555,
        "name": "Tom",
    },
    {
        "id": -999,
        "name": "Lol",
    },
);
print(users10[1]["id"]);
print(users10[0]["name"]);
users10[1]["id"] = 777;
users10[1]["name"] = "Lol and Lol";
print(users10);
print(users10[1]["name"]);
print(users10[1]["id"]);
super_lol = "Mega lol";
users10[1]["name"] = super_lol;
print(users10[1]["name"]);
new_lols = (-7, 0, 222);
print(id(new_lols));
new_lols2 = (999, 999);
new_lols = new_lols.__add__(new_lols2);
# new_lols = new_lols+new_lols2;
print(new_lols.__len__());
print(new_lols);
print(new_lols.count(999));
print(new_lols.index(-7));
print(id(new_lols));

lol_top = list(new_lols);
lol_top.insert(-1, 77777);
print(lol_top);
lol_top = tuple(lol_top);
print(type(lol_top));
print(lol_top);

print(lol_top.index(999));
zzzzz = lol_top.index(999);
print(lol_top.index(999, zzzzz+1));
print(lol_top);

my_tuple = tuple("super lol");
print(my_tuple);

my_tuple1 = tuple({"first": 888, "second": 555});
print(my_tuple1);
print(type(my_tuple1));
my_tuple2 = (-7, False, "Lol");
my_tuple3 = tuple("Hello, World");
my_tuple4 = list(my_tuple2+my_tuple3);
print(my_tuple4);

set_nums = {8, -88, 98, 8, 8};
set_dif = {99, True, "lol"};
print(set_dif);
print(type(set_dif));
print(set_nums);
set5 = {(55,55), 66, 66, 7, 66};
print(set5);
set_str = {""};
print(set_str);
set_str.clear();
print(set_str);
print(type(set_str));
set_null = set();
print(type(set_null));

photo_s = {"1900x2000", "555*666"};
photo_x = {"2000*777", "555*666"};
photo_x_s = photo_s.union(photo_x);
photo_z = {"Super"};
photo_x_s = photo_x_s|photo_z;

photo_x_s.add("Lol");
print(photo_x_s);
set_defff = photo_x.intersection(photo_s);
set_defff1 = photo_s & photo_x;
print(set_defff);
print(set_defff1);

lol_set_lo = {1, 2};
lol_set_lo1 = {5, 6, 7, 1, 0, 2};
jjj = lol_set_lo1.issubset(lol_set_lo);
print(jjj);
jjj1 = lol_set_lo.issubset(lol_set_lo1);
print(jjj1);
jjj2 = lol_set_lo1.issuperset(lol_set_lo);
print(jjj2);

print(lol_set_lo1.intersection({7, 1, 9999999}));

my_set4  = {"abc", "d", "dd","f", "y"};
print(my_set4.intersection("abcdef"));
my_cort5 = ("a", "b", "c", "d", "y");
print(my_set4.intersection(my_cort5));
print(my_set4.union("a", "b", "c", "d", "y"));
print(my_set4.discard("abc"));
print(my_set4);
print(my_set4.remove("dd"));
print(my_set4);
my_set7 = my_set4.copy();
my_set7.add("qwerty");
print(my_set7);
print(my_set4);
my_set4.add("megalol");
print(my_set4 & my_set7);
print(my_set7.symmetric_difference(my_set4));
my_set7.add(False);
print((my_set4 | my_set7) - (my_set4 & my_set7));
print(my_set7.symmetric_difference(my_set4));

my_int5 = {88, -77, 123, 99};
my_int5.add(-666);
print(my_int5);
print(type(my_int5));
my_int6 = {-44, -123, -77, 99, -666};
my_int7 = my_int6 & my_int5;
print(my_int7);
list_convert = list(my_int7);
my_int7 = list(my_int7);
print(type(list_convert));
print(type(my_int7));

my_range = range(10);
my_range2= range(2, 17, 3);
print(my_range);
print(type(my_range));
print(list(my_range));
print(my_range2);
print(list(my_range2))
print(my_range2);
print(my_range2[1]);
print(my_range2[2]);
print(my_range2[3]);
print(my_range2[4]);
print("!!!!!")

cc = range(87, 100, 3);
for xxx in range(2, 20, 3):
    print(xxx);

for xxxx in range(99, 103):
    print(xxxx);

print(type(cc));
print(cc[-1]);
for xxx in cc:
    print(xxx);
    print(list(cc));

print(tuple(cc));
print(set(cc));
print(type(cc));

print(dir(cc));
print(cc.count(90));
print(cc.index(93));
print(cc.start);
print(cc.stop);
print(cc.step);
print(cc.count(55555));

cars = ["Tesla", "BMW", "Audi", "Kamaz"];
price = [55, 30, 25, 111];
in_office = (True, False, False, True)
cars_price_zip1 = list(zip(cars, price, in_office));
cars_price_zip2 = list(zip (in_office, price, cars));
print(cars_price_zip2);
print(type(cars_price_zip2));
cars_price_zip5 = dict(zip(cars, price));
print(cars_price_zip5);

int_66 = 66;
num_66 = 66;
num_66 += 10;
print(id(66));
print(id(int_66));
print(id(num_66));
print(num_66)
print(id(76))
print(int_66)

about_lol = {
    "name": "Lol",
    "age": 1000.6,
}
lol_clone = about_lol;
about_lol["Gamer"] = True;
print(about_lol);
print(lol_clone["Gamer"]);
lol_clone["Gamer"] = False;
print(lol_clone);

lol_not_clone = {
    "name": "Lol",
    "age": 1000.6,
};
print(str(id(lol_not_clone)) + " and \n" + str (id(about_lol)));
copy_lol_clone = lol_not_clone.copy();

lol_mem = {
    "name": "Xa-Xa",
    "exchange": [],
}
lol_mem2 = lol_mem.copy();
lol_mem["exchange"].append("mem mem mem"),
print(lol_mem2["exchange"]);
print(lol_mem["exchange"]);
print(lol_mem2);
print(lol_mem);


lol_mem["exchange"].clear();
print(lol_mem)
lol_mem3 = deepcopy(lol_mem);
lol_mem["exchange"].append("joke");
lol_mem["exchange"].append("Bla-bla-bla");
print(lol_mem3);
print(lol_mem);
print(lol_mem2);

a = 5
b = 10

c = 100;
d = 101;


def nyn(x, y):
    return x * y;

print(nyn(a,b))

def non(x, y):
    y += 100;
    c = x + y;
    print(c);

non(a, b);
print(type(non));

f = nyn(c, d);
print(f)

pers_lol = {
    "name": "Tom",
    "age": 30,
}
print(pers_lol["age"]);
def increase_lol(xxx):
    xxx["age"] +=100;
    print(id(xxx))
    return xxx;

print(pers_lol["age"])

increase_lol(pers_lol)

print(pers_lol);
print(pers_lol["age"]);
print(id(pers_lol))

def method2(yyy):
    yyy_copy = yyy.copy();
    yyy_copy["age"] += 1000;
    return yyy_copy;


lol_method2 = method2(pers_lol);
print(lol_method2);
print(pers_lol);
print(pers_lol["age"]);
print(lol_method2["age"]);


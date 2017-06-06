import sys
from z3 import *
array = [ BitVec('a%i'%i,8) for i in range(0,17)] #0~16.
Str = ""
sTemp = ""
s = Solver()
s.add(array[0] * -469141 + array[1] * 408514 + array[2] * 428986 + array[3] * 103869 + array[4] * 466565 + array[5] * 648745 + array[6] * 122207 + array[7] * 398062 + array[8] * 723048 + array[9] * 288564 + array[10] * 548719 + array[11] * 397546 + array[12] * -417512 + array[13] * 847445 + array[14] * 618037 + array[15] * 131763  == 464009506)
s.add(array[0] * 555250 + array[1] * -529838 + array[2] * 416969 + array[3] * 663660 + array[4] * 391591 + array[5] * 471484 + array[6] * 718531 + array[7] * 435812 + array[8] * 370454 + array[9] * 635503 + array[10] * 421950 + array[11] * -576380 + array[12] * 952879 + array[13] * 517643 + array[14] * 887909 + array[15] * 338372  == 571027945)
s.add(array[0] * 742509 + array[1] * 233247 + array[2] * -258594 + array[3] * 125426 + array[4] * 781993 + array[5] * 280801 + array[6] * 339841 + array[7] * 421393 + array[8] * 385718 + array[9] * -788560 + array[10] * 718939 + array[11] * 703230 + array[12] * 552358 + array[13] * 253329 + array[14] * 651345 + array[15] * 107608  == 533276094)
s.add(array[0] * 599519 + array[1] * 968314 + array[2] * 587620 + array[3] * -891110 + array[4] * 439798 + array[5] * 306151 + array[6] * 326922 + array[7] * -626604 + array[8] * 841654 + array[9] * 648872 + array[10] * 119336 + array[11] * 710885 + array[12] * 982867 + array[13] * 907246 + array[14] * 949258 + array[15] * 641728  == 574037396)
s.add(array[0] * 956845 + array[1] * 124204 + array[2] * 667155 + array[3] * 655190 + array[4] * -221357 + array[5] * 823348 + array[6] * 976584 + array[7] * 507075 + array[8] * -528260 + array[9] * 611875 + array[10] * 126657 + array[11] * 980618 + array[12] * 765204 + array[13] * 594354 + array[14] * 904578 + array[15] * 364723  == 688059830)
s.add(array[0] * 479020 + array[1] * 492198 + array[2] * 172185 + array[3] * 735171 + array[4] * 614702 + array[5] * -315459 + array[6] * 361775 + array[7] * 372708 + array[8] * 780683 + array[9] * 381112 + array[10] * 983594 + array[11] * 763550 + array[12] * 204710 + array[13] * 849204 + array[14] * 321631 + array[15] * 977907  == 736496777)
s.add(array[0] * 873408 + array[1] * 805138 + array[2] * 633098 + array[3] * 994765 + array[4] * 628486 + array[5] * 609682 + array[6] * -418193 + array[7] * 156746 + array[8] * 137909 + array[9] * 444850 + array[10] * 953717 + array[11] * 803114 + array[12] * 855557 + array[13] * 774647 + array[14] * 984189 + array[15] * 334577  == 785321830)
s.add(array[0] * 183198 + array[1] * 972727 + array[2] * -969748 + array[3] * 697900 + array[4] * 288186 + array[5] * 331524 + array[6] * 970608 + array[7] * -968870 + array[8] * 528988 + array[9] * 870554 + array[10] * 648772 + array[11] * 550050 + array[12] * 636110 + array[13] * 870403 + array[14] * 444309 + array[15] * 425870  == 565242486)
s.add(array[0] * 675541 + array[1] * 977407 + array[2] * 420636 + array[3] * 220379 + array[4] * 503441 + array[5] * 655181 + array[6] * 193478 + array[7] * 541351 + array[8] * -100031 + array[9] * 147195 + array[10] * 260817 + array[11] * -855588 + array[12] * 738194 + array[13] * 161358 + array[14] * -190166 + array[15] * 821392  == 320351102)
s.add(array[0] * 134085 + array[1] * 976266 + array[2] * 519292 + array[3] * 322272 + array[4] * -224142 + array[5] * 406253 + array[6] * 291142 + array[7] * 569482 + array[8] * 193159 + array[9] * -756266 + array[10] * 119532 + array[11] * 729270 + array[12] * 626670 + array[13] * 380194 + array[14] * -971492 + array[15] * 218563  == 272757944)
s.add(array[0] * 357601 + array[1] * 392128 + array[2] * 338943 + array[3] * 761043 + array[4] * 947309 + array[5] * 432421 + array[6] * 218746 + array[7] * 863693 + array[8] * 395968 + array[9] * 379563 + array[10] * -635633 + array[11] * 134162 + array[12] * -440921 + array[13] * 642151 + array[14] * 855555 + array[15] * 475007  == 544380221)
s.add(array[0] * 618418 + array[1] * 291199 + array[2] * 613631 + array[3] * -742560 + array[4] * 513804 + array[5] * 721125 + array[6] * 312043 + array[7] * 606964 + array[8] * 477391 + array[9] * 247927 + array[10] * 252586 + array[11] * -920413 + array[12] * 528121 + array[13] * 224078 + array[14] * 138977 + array[15] * 785723  == 304673327)
s.add(array[0] * 432559 + array[1] * 377920 + array[2] * 463118 + array[3] * 296220 + array[4] * 710341 + array[5] * -581864 + array[6] * 159913 + array[7] * 922661 + array[8] * 777779 + array[9] * 611899 + array[10] * 956823 + array[11] * 218700 + array[12] * -254050 + array[13] * 728730 + array[14] * 510059 + array[15] * 772468  == 646913676)
s.add(array[0] * 919930 + array[1] * 123690 + array[2] * 431381 + array[3] * 433734 + array[4] * -661167 + array[5] * 643424 + array[6] * 857050 + array[7] * 138559 + array[8] * 707703 + array[9] * 109636 + array[10] * 958972 + array[11] * 235825 + array[12] * 150067 + array[13] * -914301 + array[14] * 837900 + array[15] * 482626  == 461545648)
s.add(array[0] * 292221 + array[1] * 301018 + array[2] * -678846 + array[3] * 818914 + array[4] * 699234 + array[5] * 655112 + array[6] * -741575 + array[7] * 477013 + array[8] * 267011 + array[9] * 614751 + array[10] * 512065 + array[11] * 337413 + array[12] * 343481 + array[13] * 838477 + array[14] * -926234 + array[15] * 179763  == 324605988)
s.add(array[0] * 778519 + array[1] * 357615 + array[2] * 513498 + array[3] * 439687 + array[4] * 817391 + array[5] * 370548 + array[6] * -478246 + array[7] * 525094 + array[8] * 296537 + array[9] * 353570 + array[10] * 660919 + array[11] * 346604 + array[12] * 267872 + array[13] * 415171 + array[14] * 645582 + array[15] * -376445  == 531420615)
for i in range(1,17):
    s.add(And(array[i] >= 32 , array[i] <= 127))
print s.check()
m = s.model()
for i in range(0,17):
    sys.stdout.write(chr(m.eval(array[i]).as_long()))



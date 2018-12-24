
#ifndef             MCTEST
#define MCTEST

# define  MC1
#            define       MC2

#ifdef              MC1

#define AAAAAAA 0x2FLU
/*cmment start*/#define /*this is // "string" comment*/ data2 2.5f
/* */#define date3 "this is a data \"yayaya~\""  L" L--an/*o*/ther //data ahhah" "aaa\n"
#define data4 true
#define TABTAB "with a tab \t"

/*"/*"*//*"*/
/* "string" */

// "string comment" /**/

// //
#ifdef          MC2 /* "*/

#       define               data5 'a'
# define data12 { {'x', {'y', 'z',}, -200l, "abc"}, {+1.5e-2,L"def"}, {5.6f,/*"xixi"*/ "7.2"}} //  "浮点与字符串组成的结构体初始化聚合， 再进一步聚合组成了数组"

#       else

#define data10 {5.0, 7.5, 3.8}
#define data6 'c'

#       endif //end MC2


#else

#define data1 -.010e+4f  /* this is float
may be changed
*/
#define data2 200Lu
/* #define date3  false */
#define data4 "this is \'a\' data" L" anothe\\//r data" "12345\t56\t\n" // line comment


#ifdef MC2

#define data5 'B'
#define data9 {1UL, 6lu, 3LU}
#define data7 0xaf

#else

#       define data20 '\t'
#   define  data21 '\"'
#define date22          '\n'
#define XXXXXXXX { 1.0f, { {2.0, "nice" "??" "\t0x12"  "012"},{5.6f, "7.2"},"{}}"}, L"abc\n", { '{', ',', 1.0f, 0xab, {1}, L"hello}, world"} }

#endif //end MC2

#           endif //MC1

#ifdef MC2
#undef MC2
#endif

#define OCT 0100U
#define HEX 0X1fe
#define DEC 12306L

#define data11 { 0.01e+3, { {-0x2f, "nice/*not comment ..//*/" " /*///*/*/*/ \t comments !!!\"", +0x22, },{+.6e-2f, "7.2" , "032LU", +1.23, {-0x32}, } ,"{}}", -012} , "abc", 'D', '\t', { '{', ',', 1.0f, 0xab, {1}, L"hello}\"\', world"} }


#endif // !MC_TEST
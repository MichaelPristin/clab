"""Generated lookup tables for the legacy converters.

DO NOT EDIT: produced by tools/gen_tables.py at packaging time (see
encoding.py for the loader).
"""

DELIMITER_MAP = {",": "comma", ";": "semicolon", "\t": "tab"}
QUOTE_STYLES = ("minimal", "all", "nonnumeric", "none")
DATE_FORMATS = ("%Y-%m-%d", "%d/%m/%Y", "%Y%m%dT%H%M%S")

# master encoding table (base85 framing, zlib-wrapped, marshalled for
# fast import; consumed by encoding._load_legacy_tables)
ENC_TABLE = (
    b"""
    c-
    oy;Yj6|S6~1>L+FfaP^{{2jU}Iw=6a{Q!64S&u0a_r%j@<@GQ{1Gk(5`I>y;#Zk5i8?P(?J5ySe`UBw4K3ef5aV_4xRjHes(
    6!B;nD)Q970veq_@8(Vvb2nZlTMruVMAiysoqbTxDK+<VSF_nhyZbMES&VAaE{yzfbf%mN7nA=vN`K!!3g2qgG>c$p~9U0%`
    aBPHT(&_{7ti@LnB0)jEJ3CQ#|ppX!pK%)^bN}d2C&`YVn`$7Iqq?B*OL_tKMFxP=egE91D62ioX$w^F_v6RM~j7bcWD4ydn
    *JiBUi8;m?CUj0Qtq~}qZcnjdy&&cUOjt}DhMs-xGD{hI`7@a8F0(8jF1M`J*saR&su~Ld#?WPOX5GL1DI;>paNJ=86ETz>h
    5;;4He+eLTx@JPCx;AE4#SsPL$BH(tU-
    9)tNf_3!fGInt>jyDhl+yAwJO4zc$GR#>M_}5NGsRwtF7e>^5nD34{nS%{}W@b+Su1>9FJfKs@CR^%Yft&;+qZSdc&7>5ebi
    jPT5ihx?+M17@=xL8;p${##$rt{2Q1g5%I6CZk)^{ZUKKs0Gt)hif657ZKxGM3538oQG3H=aZDtk_9l~r_NI~~2hw8Dvax9-
    c%9Q*MUtAJg7%G?5}|99k&{o5Q-
    +)jR+Ny_Xx_PTUT;=<OPc_}>hf9>FzDJSMYEeW&Iaqs+mT>Raj*Kv?$xkS8UT{%cjj|e4zF%1zdCJ|n9lNOu{v6#Fit=)2o8
    cbevD3s=0L)2#07%eOT^_ZfdH-BlQ<p8c91kpn1VY>>~7YzgUuzR7KztwpeO_lDH_KjX+K>C!BigwxN;F%S4H?VEEh{_iCBn
    W+hb17rthC*k<DjHtY;<r6~`klpNMBEAJ`{VN%7nyL8=&EmAz8sYV=V}wr{kNwoaHN=as6<r0(H*T+8fTt?zx#mbNL@l$f%n
    Yy+g^dYe5b;Hy6^Ji7YJ*w}3J0e*s4UN56nt7|D;|7Sk(Mn2Z9%f}Z=?6+ltl4^0DjccRvRsCusI%C?e2_!^)z43tq^beeMQ
    Vv_uEAj-
    $z^NOLG}}NNju3b~L_Z`8m9$ZnWF&Ed88@x3iWA6ol6i|kE59moBe0zHsehHUt$9E7pEBO>hae>kK&j?!Hpy|tJ79CtJYfz#
    UjoZb6GjI}S|%*Pz2$2Of{3-0ClN~bM8j%(xoE~f`Dh-Ug}1&pk0mNpRG3iV$#IAKM6)~G?3RwZzu)2R>2M$G^O{u{P~j;Ro
    >7TJTqXS@l1llMK{SkwsbnmGhC|UfT0g3i!)OEtRYEx#05$-
    Y>EXmc^K&Yr$gz;mFDtk!jGGP}J=)=pt1zt6exH9xKJJAoD~|@^iT>!Rak?cKk498DlE;~bM5aJQk|SsX|C*Z_e~{q&?A}+1
    yi4kLauQbqQKA~?5*1ISi6B#A-ndhP+~azUL`qZuUZM4lk%VRTwv@UXCDRo~&xoM#xVs3SsF&+iaFHwD!5H%2i$)R%l;-
    1OF?rnPi^W0#zb_GpMp`j?UP7fLU&5y{L$Xhjm3W>kV#y=|VL3XS2mtiW<7HHFSP6v!CtDQx^stN$kujK~D-
    10ShhuToBuD&FNmd!OAR3b+Dy1OHURpI3EvWFcN)-<-
    s>0zoM!TV5a&mH6==8_W^bg6Q81myqmFSO+i~R#FouR1T7mB~w(jVJ}bmRCh%Y#X9o8S7St!h@B5f^RS7i`;eHha!lGut=QH
    wWK&W6|kdaC+xGS?BItjpvqk?=4qnfdO{UJwVyT)PaH-2o=-
    4>E1=Yae;4~Yn%7o;v2L4u0_6mfp5Pm{e$0o53K*jqx4LA7H1Ni1zOKuRgGF#1COaB*o&~`4vqTd7(N3pRF2}9@bOJ5uizRZ
    `bXA<J%Sr<yuKKAfgtTQOO;jc9(-`8y5TN>c;qUO=)D}r--
    ^FrEZ{s>P5v5IlY>P+zTBt6m<mHG^escPw_fShHj1JmjgQ4uHX(;&1A&mNQuxqSIu!LuapXw1@+wv&2jzsy#uLhbCN>R*SKe
    |0)wqH$UzIt7&I|>l(s7hv2~CJAo<-%H7>FuiZ3b68RZNPQFEON=<<XcgA`Qo7Md`+7Op>f64;73CBB~iJ!M;fWMP<XjQ!--
    WC|^;Ysa#?R=T#swsM5!gI||x4;Zsl=jwpeI?6oV}zmL~3!5{3(Pchkt$!l8l14Am5RVXPx!gERy`h?PhNBB%Mkdz-
    _@<WWjUCYx|&wljiM>e30uQZyt1r^Xkl%ACJHYMDq#M@K_;tLc>TXVc^x+~rFE9HD|3Km!(TBl!4znXdGd|yrwOR=J3I-
    CyQs@-
    *U+h2D4dB+FMS#f{PYM&lUkDY%rXRDZHXV{!*pFWj7wJ6pvi1k@<>)h4_aoZXteumEp)^D5^&NO+T;38>PuEII{{LJ(3>`lR
    xJIxkMt6ce9sJpQHE}&^Q@{yo8_Z_=4b8>cYW^l3UsfDVi=Iz<49rMSt_T2>lg+uV_$z1K0OD|n~Y3|@}dlqYVEg)~JKlEm6
    4`yJdX~vW}J;U86vF3vUjjR@U6D{O;Vfs+|P^Rg8*XR7<3yqgN7d@ADUfel1y6EXx@N{H7ogWTnHyuvF9BZDoq%D~Pb5zRm1
    ?#>e*fWi@o*B>V&Y7JTPS3Ty-~L|ve8nF+K5u&VYQ=}lLgT)yWB*^9vch5HALseB5u<)2eI(<%;Fvp*I`Rd-
    9l67K5dNHbnoiRx|9SJ|fhC6hH^Fk9g-
    R>uT;j#4gM}^Y6;iJhL7M8rz}QOyb1Z9b!@#s&J({yQ@Bv+@oP%>s@0l*v%~vkeG=E`h!Em%{N(CB-uF2C6z8!;rccN;htxK
    $ks+qPv{I+3b3LRH9KBy@c3tY?hS&Zg48u|~vwz`lG=gzqr=GrdusRJp0`f#Rg`p841%(<8En{lidiHBcXDzQ0XiRG~&0q<a
    |xeEl&`7J>SHRxmn=WScVm(DG-{WJY@$L1Te&gKlU634sd2X`uJkp;oIWUE9L1m}MXHE8kj{YE_=-
    5vW9Z^QfBm*ZcfqWF!o%K<*BsOZ`XKHBH*CW*god#Y;>{V~rX{^RQJ^4)FVlO|`koBZTC7V)2MW?ly1GsfNH0-
    x>N+{2UC7#8u@99-
    8H@>(6lbgS6)40&xg#B>kc4Y+H2vAOFc*WE~8=PliJ^z}L#^KQDkg}MGTgDhWf<GNoUuXjR3Zve4}BX3x@zr2UI(GD@chwCB
    e8~X^v--
    HnHHwhB+ESBEn=^iI@(@r8!ZaOvU;(E4`H=7`$y<U?N(b{F$7eik^LyGb<+&pk&(E8{ffpQG<xMeJ}o#Ci79FkvD-qJ1()Hs
    eHf-
    r*+m7|G0``XW6OCQTr+y$Weh#6f)Vi%^SZu2B@*VF}}z0gM>gqJAOFAqM*F*XD{9^o8;T=6Qn#CX8_bSwEM*h>Bn@OA$#
    """
)

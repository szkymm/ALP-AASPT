#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
THIS FILE IS CORE PART OF ALPS BY MATT BELFAST BROWN
Azur_Lane_Plan_Strategy.py - The core part of this tool.
ALP-AASPT（Azur Lane Plan Annealing Algorithm Strategy Planning Tool）.
The code is from `azurlanekeyan` product by tianqianzhiyang, Licensed under the Mulan PSL V2.
Copyright (C) 2022 tianqianzhiyang
Author: tianqianzhiyang
bilibili: https://space.bilibili.com/337285187/
git_url: https://gitee.com/iamtianqianzhiyang/azurelanekeyan

Author: Matt Belfast Brown
E-mail: thedayofthedo@gmail.com
Create Date: 2023-03-04
Version Date: 2023-03-04
Version: 0.0.1α1

THIS PROGRAM IS FREE FOR EVERYONE,IS LICENSED UNDER GPL-3.0
YOU SHOULD HAVE RECEIVED A COPY OF GPL-3.0 LICENSE.

Copyright (C) 2023 Matt Belfast Brown

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from AzurLaneToolLib.mode import mode_SRS_Ptl
import PySimpleGUI as sg
import mode

meta_data = []
list_firt = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", 1]


# define dictionary
def fun_oupt_plst():
    # mthd_mtrl = eval(input("请输入物资限制方式：\n"))  # 物资限制方式 31 1
    # numb_mtrl = eval(input("请输入物资限制数目：\n"))  # 物资限制数目 31 2
    # mthd_mdcb = eval(input("请输入魔方限制方式：\n"))  # 魔方限制方式 32 1
    # numb_mdcb = eval(input("请输入魔方限制数目：\n"))  # 魔方限制数目 32 2
    # mthd_kssr = eval(input("请输入金船限制方式：\n"))  # 金船限制方式 33 1
    # numb_kssr = eval(input("请输入金船限制数目：\n"))  # 金船限制数目 33 2
    # mthd_ksur = eval(input("请输入彩船限制方式：\n"))  # 彩船限制方式 34 1
    # numb_ksur = eval(input("请输入彩船限制方式：\n"))  # 彩船限制数目 34 2
    # mthd_tcur = eval(input("请输入彩装限制方式：\n"))  # 彩装限制方式 35 1
    # numb_tcur = eval(input("请输入彩装限制数目：\n"))  # 彩装限制数目 35 2
    # mthd_mtut = eval(input("请输入心智限制方式：\n"))  # 心智限制方式 36 1
    # numb_mtut = eval(input("请输入心智限制方式：\n"))  # 心智限制方式 36 2
    # numb_hssr = eval(input("请输入金船已有数目：\n"))  # 金船已有数目 38 1
    # numb_hpur = eval(input("请输入彩船已有数目：\n"))  # 彩船已有数目 39 1
    # numb_stto = eval(input("请输入2-4期完成船数目：\n"))
    # numb_fifo = eval(input("请输入5期已完成船数目：\n"))
    mthd_mtrl = 1  # 物资限制方式 31 1
    numb_mtrl = 20000  # 物资限制数目 31 2
    mthd_mdcb = 1  # 魔方限制方式 32 1
    numb_mdcb = 1  # 魔方限制数目 32 2
    mthd_kssr = 1  # 金船限制方式 33 1
    numb_kssr = 100  # 金船限制数目 33 2
    mthd_ksur = 2  # 彩船限制方式 34 1
    numb_ksur = 150  # 彩船限制数目 34 2
    mthd_tcur = 0  # 彩装限制方式 35 1
    numb_tcur = 6.3  # 彩装限制数目 35 2
    mthd_mtut = 0  # 心智限制方式 36 1
    numb_mtut = 7000  # 心智限制方式 36 2
    numb_hssr = 975  # 金船已有数目 38 1
    numb_hpur = 580  # 彩船已有数目 39 1
    numb_stto = 13
    numb_fifo = 0
    prob_plpr = (16 - numb_stto) / (5 - numb_fifo + 16 - numb_stto)
    dic_polc_rstr = {
        "mthd_mtrl": mthd_mtrl, "numb_mtrl": numb_mtrl, "mthd_mdcb": mthd_mdcb, "numb_mdcb": numb_mdcb,
        "mthd_kssr": mthd_kssr, "numb_kssr": numb_kssr, "mthd_ksur": mthd_ksur, "numb_ksur": numb_ksur,
        "mthd_tcur": mthd_tcur, "numb_tcur": numb_tcur, "mthd_mtut": mthd_mtut, "numb_mtut": numb_mtut,
        "numb_hssr": numb_hssr, "numb_hpur": numb_hpur, "prob_plpr": prob_plpr, "time_algr": 1000,
    }
    base_ksen = mode_SRS_Ptl.fun_anel_algr(1, dic_polc_rstr)
    fite_calu = mode_SRS_Ptl.FitCal(dic_polc_rstr)
    valu_firt = mode_SRS_Ptl.fun_gain_valu(base_ksen.keyg_kfir)
    valu_seco = mode_SRS_Ptl.fun_gain_valu(base_ksen.keyg_ksec)
    valu_thir = mode_SRS_Ptl.fun_gain_valu(base_ksen.keyg_kthi)
    dic_plan_fist = mode_SRS_Ptl.FitCal.iir_cuin_calc(fite_calu, valu_firt, dic_polc_rstr, 0)
    dic_plan_seco = mode_SRS_Ptl.FitCal.iir_cuin_calc(fite_calu, valu_seco, dic_polc_rstr, 1)
    dic_plan_thir = mode_SRS_Ptl.FitCal.iir_cuin_calc(fite_calu, valu_thir, dic_polc_rstr, 2)
    list_prob = [dic_plan_fist, dic_plan_seco, dic_plan_thir]
    # numb_fitn = mode_SRS_Ptl.FitCal.iir_fitn_calc(fite_calu,1,list_prob)
    dic_oupt_plan = mode_SRS_Ptl.FitCal(dic_polc_rstr).iir_gain_opls(1, list_prob)
    print("金船满破阶段")
    fun_gain_proj(dic_plan_fist)
    print("彩船满破阶段")
    fun_gain_proj(dic_plan_seco)
    print("做彩装备阶段")
    fun_gain_proj(dic_plan_thir)


def fun_gain_proj(dic_plan_numb):
    list_tact = dic_plan_numb["rank_list"]
    for i in range(30):
        p = i // 10
        p *= 3
        if i == dic_plan_numb["lift_coma"]:
            continue
        elif i >= dic_plan_numb["lift_coma"]:
            j = i - 1
            j = list_tact[j]
        else:
            j = list_tact[i]
        if j == 10:
            print("10.后续刷新！")
            break
        print(j, end=".")
        print(mode.list_pldt[int(j)]["plan_name"])

#define var
sg.theme("SystemDefaultForReal")
llay_prna =[
    [sg.Text("本工具针对UP主天谴之羊（uid：337285187）所提出的退火策略算法进行GUI表现。使用时请详细对照下文说明。")],
    [sg.Text("退火算法的科研策略建议工具")],
    [sg.Text("物资消耗"),sg.Combo(["滥用","奢侈","节俭","尽量不用"],key="mthd_mtrl"),sg.Text("上限"),sg.Input(size=(20,20),key="numb_mtrl")]
]
fun_oupt_plst()

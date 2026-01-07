# LSR-undefined

## 基本信息

- LSR 编号 ???
- 标题 ???
- 作者 Ziyang-Bai
- 状态 ??
- 类型 ???
- 创建日期 ??-??-2024
- 归属项目 ??

## 1. 范围（Scope）

本推荐规范定义了一种基于文本的电路描述语言，用于描述电子电路系统的结构信息，包括但不限于：

* 电路元件（Components）
* 元件引脚（Pins）
* 电气网络（Nets）
* 参数与数值（Parameters）
* 层次化结构（Hierarchy）

该语言旨在为以下场景提供统一、清晰的文本表示：

* 电子电路的文本描述与审阅
* 原理图的文本化等价表示
* 电路结构的版本控制与比较
* 与 SPICE Netlist 之间的结构等价互操作

---

## 2. 设计目标（Design Goals）

### 2.1 可读性（Readability）

语法应优先保证人类可读性，避免 SPICE Netlist 中常见的隐式约定和语义重载。

### 2.2 结构化（Structured Representation）

语言应显式表达电路的结构关系，而非依赖线性文本顺序。

### 2.3 可互操作性（Interoperability）

语言应支持与主流 SPICE Netlist 之间的双向转换，保证电路在结构层面的等价性。

### 2.4 可实现性（Implementability）

规范应允许使用常规编程语言（如 C/C++、Rust、Python）实现解析器与生成器，不要求图形界面或专有运行环境。

---

## 3. 术语定义（Terminology）

| 术语 | 含义 |
|------|------|
| Component | 具有类型、引脚和参数的电路元件 |
| Pin | 元件上的一个连接端点 |
| Net | 一个或多个 Pin 之间的电气连接 |
| Circuit | 元件与网络的集合 |
| Subcircuit | 可复用的电路定义单元 |
| Parameter | 元件或电路的可配置数值 |

除非另有说明，本规范中使用的术语均不区分大小写。

---

## 4. 基本语法约定（Lexical Conventions）

### 4.1 字符集

源文件应采用 UTF-8 编码。

### 4.2 注释

```
# 单行注释
// 单行注释
```

### 4.3 标识符

* 由字母、数字、下划线组成
* 不得以数字开头
* 区分大小写（推荐实现支持大小写敏感）

---

## 5. 核心抽象模型（Abstract Circuit Model）

实现应在解析阶段构建以下抽象模型：

### 5.1 Component

* 唯一名称
* 类型（Resistor, Capacitor, Subcircuit Instance 等）
* 引脚列表
* 参数集合

### 5.2 Net

* 唯一名称
* 连接的 Pin 集合

### 5.3 Pin Reference

表示为：

```
<ComponentName>.<PinName>
```

---

## 6. 基本语法（Core Syntax）

### 6.1 元件声明

```
component R1 : Resistor {
    pins: a, b
    value: 10k
}
```

### 6.2 网络声明

```
net N1 {
    R1.a
    C1.a
    V1.positive
}
```

### 6.3 简写连接语法（Optional）

```
R1.a -> N1
C1.a -> N1
```

---

## 7. 层次结构（Hierarchy）

### 7.1 子电路定义

```
subcircuit Amplifier(in+, in-, out) {
    component R1 : Resistor { value: 10k }
    component R2 : Resistor { value: 10k }
    
    net N1 { R1.a, R2.a }
}
```

### 7.2 子电路实例化

```
component A1 : Amplifier {
    in+  -> Vin
    in-  -> GND
    out  -> Vout
}
```

---

## 8. SPICE Netlist 互操作（Informative）

### 8.1 结构等价性

本语言与 SPICE Netlist 的互操作以结构等价为目标，而非文本等价。

### 8.2 映射原则（示例）

| 本语言 | SPICE |
|--------|-------|
| component R1 : Resistor | R1 |
| net N1 | node |
| subcircuit | .subckt |

---

## 9. 合规性（Conformance）

一个实现若满足以下条件，可被视为符合本规范：

* 能解析并构建抽象电路模型
* 能检测并报告语法与结构错误
* 能导出等价的 SPICE Netlist（核心子集）

---

## 10. 扩展性（Extensibility）

实现可以在不破坏核心语义的前提下引入扩展，例如：

* 仿真指令
* 参数表达式
* 工艺库绑定

扩展应避免与核心语法产生歧义。

---

## 11. 非目标（Non-Goals）

本规范不定义：

* 图形化原理图表示
* PCB 布线规则
* 仿真算法或数值模型

---

## 12. 参考（References）

* SPICE User's Guide
* IEEE Std 315（电路符号）

---
Copyright © 2024-2026 Ziyang-Bai. All rights reserved.

This document, and the language specification contained herein, is the
exclusive intellectual property of Ziyang-Bai. All rights are reserved.

Ziyang-Bai hereby retains the right to grant, modify, or revoke
permissions to use, copy, reproduce, distribute, or implement this
document or any part of the language specification at their sole discretion.

No part of this document may be reproduced, transmitted, or used for
implementation purposes without the prior written consent of Ziyang-Bai.

For inquiries regarding licensing or permission to use this specification,
please contact Ziyang-Bai at baiziyang2022@yeah.net.

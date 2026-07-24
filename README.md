# XYZ Bank E-Banking UI Test Automation (XYZ Bankası E-Bankacılık Test Otomasyonu)

*(Scroll down for English version) / (İngilizce versiyonu için aşağı kaydırın)*

Bu depo, bir bankacılık ve finans uygulaması olan "XYZ Bank" üzerindeki kritik kullanıcı akışlarını (Müşteri Ekleme, Yönetici İşlemleri vb.) doğrulamak için geliştirilmiş otomatik UI test senaryolarını içerir.

Bir Yazılım Test (QA) Uzmanı olarak bu projeyi; finansal sistemlerde test güvenilirliğini sağlama, test verilerini modüler hale getirme (Constants) ve ekran görüntüleri yardımıyla **test kanıtı (test evidence)** oluşturma yetkinliklerimi sergilemek amacıyla geliştirdim.

## 🚀 Kullanılan Teknolojiler
- **Dil:** Python
- **Otomasyon Aracı:** Selenium WebDriver
- **Mimari:** Konfigürasyonları ve element yapılarını ayıran Constants (Sabitler) yapısı.

## 📁 Proje Yapısı
- `test_AddCostumer.py`: Yeni hesap/müşteri oluşturma işlevini test eden otomasyon betiği.
- `test_AddManager.py`: Banka yöneticisi yetkilerini ve akışlarını test eden test senaryoları.
- `Constants/`: Test verilerini ve UI locator'larını (Xpath, CSS vb.) barındıran dizin.
- `2023-09-07/`: Test koşum sonuçlarını ve görsel test kanıtlarını (ekran görüntüleri) barındıran rapor klasörü.

## 🛠️ Kurulum ve Çalıştırma

1. Projeyi bilgisayarınıza indirin:
   ```bash
   git clone https://github.com/YunusBasak/XYZBank.git
   ```
2. Gerekli kütüphaneleri kurun:
   ```bash
   pip install selenium
   ```
3. Test betiklerini çalıştırın:
   ```bash
   python test_AddCostumer.py
   python test_AddManager.py
   ```

---

# XYZ Bank E-Banking UI Test Automation (English)

This repository contains automated UI testing scenarios designed to validate critical user flows (such as Add Customer, Manager Login) on a financial application named "XYZ Bank".

As a Quality Assurance (QA) engineer, I developed this project to showcase best practices in ensuring test reliability within financial systems, isolating test data, and generating visual **test evidence** (screenshots).

## 🚀 Tech Stack & Tools
- **Language:** Python
- **Automation Tool:** Selenium WebDriver
- **Architecture:** Constants-driven approach for modular configurations and element locators.

## 📁 Project Structure
- `test_AddCostumer.py`: Automation script validating new customer creation flows.
- `test_AddManager.py`: Script focusing on bank manager workflows and authentications.
- `Constants/`: Directory containing test configurations, data, and locators.
- `2023-09-07/`: Contains sample test execution evidence (screenshots representing automation output).

## 🛠️ Setup & Execution

1. Clone the repository:
   ```bash
   git clone https://github.com/YunusBasak/XYZBank.git
   ```
2. Install the required dependencies:
   ```bash
   pip install selenium
   ```
3. Run the automation scripts:
   ```bash
   python test_AddCostumer.py
   python test_AddManager.py
   ```

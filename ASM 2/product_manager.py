import json

# 1. Hàm tải dữ liệu từ file 
def load_data():
    try:
        with open('products.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError: 
        return []

# 2. Hàm ghi dữ liệu vào file 
def save_data(products):
    with open('products.json', 'w', encoding='utf-8') as f:
        json.dump(products, f, ensure_ascii=False, indent=4)

# 3. Hàm thêm sản phẩm mới
def add_product(products):
    print("\n--- THÊM SẢN PHẨM MỚI ---")
    # Tự động tạo mã ID dựa trên số lượng hiện có [cite: 93]
    id_moi = f"LT{len(products) + 1:02d}" 
    ten = input("Nhập tên sản phẩm: ")
    thuong_hieu = input("Nhập thương hiệu: ")
    gia = int(input("Nhập giá: "))
    so_luong = int(input("Nhập số lượng tồn kho: "))
    
    moi = {
        "ID": id_moi,
        "Ten": ten,
        "ThuongHieu": thuong_hieu,
        "Gia": gia,
        "SoLuong": so_luong
    }
    products.append(moi)
    print(f"Đã thêm sản phẩm thành công với mã: {id_moi}")
    return products

# 4. Hàm cập nhật sản phẩm 
def update_product(products):
    ma_tim = input("Nhập mã sản phẩm cần sửa (VD: LT01): ")
    cho_sua = next((p for p in products if p['ID'] == ma_tim), None)
    
    if cho_sua:
        print("Để trống nếu không muốn thay đổi.")
        ten = input(f"Tên mới ({cho_sua['Ten']}): ")
        if ten: cho_sua['Ten'] = ten
        # Tương tự cho các trường khác...
        print("Cập nhật thành công!")
    else:
        print("Không tìm thấy mã sản phẩm này!")

# 5. Hàm xóa sản phẩm
def delete_product(products):
    ma_xoa = input("Nhập mã sản phẩm cần xóa: ")
    for p in products:
        if p['ID'] == ma_xoa:
            products.remove(p)
            print("Đã xóa sản phẩm.")
            return
    print("Không tìm thấy sản phẩm!")

# 6. Tìm kiếm theo tên (không phân biệt hoa thường)
def search_product_by_name(products):
    tu_khoa = input("Nhập từ khóa tìm kiếm: ").lower()
    ket_qua = [p for p in products if tu_khoa in p['Ten'].lower()]
    display_all_products(ket_qua)

# 7. Hiển thị tất cả
def display_all_products(products):
    if not products:
        print("Kho hàng trống.")
        return
    print(f"{'ID':<10} {'Tên sản phẩm':<30} {'Hãng':<15} {'Giá':<10} {'Kho'}")
    for p in products:
        print(f"{p['ID']:<10} {p['Ten']:<30} {p['ThuongHieu']:<15} {p['Gia']:<10} {p['SoLuong']}")
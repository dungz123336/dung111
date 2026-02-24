import product_manager as pm

def main():
    
    products = pm.load_data()
    
    while True: 
        print("\n=== HỆ THỐNG QUẢN LÝ POLY-LAP ===")
        print("1. Xem danh sách sản phẩm")
        print("2. Thêm sản phẩm")
        print("3. Cập nhật sản phẩm")
        print("4. Xóa sản phẩm")
        print("5. Tìm kiếm sản phẩm")
        print("6. Thoát")
        
        chon = input("Mời bạn chọn chức năng (1-6): ")
        
        if chon == '1':
            pm.display_all_products(products)
        elif chon == '2':
            products = pm.add_product(products)
        elif chon == '3':
            pm.update_product(products)
        elif chon == '4':
            pm.delete_product(products)
        elif chon == '5':
            pm.search_product_by_name(products)
        elif chon == '6':
            # Lưu dữ liệu trước khi thoát
            pm.save_data(products)
            print("Cảm ơn bạn đã sử dụng. Dữ liệu đã được lưu!")
            break
        else:
            print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()
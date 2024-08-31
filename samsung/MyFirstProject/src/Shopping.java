public class Shopping {

    static int numberOfOrders = 0;
    public static void main(String[] args) {
        // 1. 누가(고객)
        // 2. 무엇을(상품)
        // 3. 얼마(가격)
        
        order(new Customer("안영희", "01012345678", null), "켄트백의 Tidy First?", 19800);
        order(new Customer("안영희", null, "david@company.comn"), "켄트백의 Tidy First?", 19800);
        order(new Customer(null, "01012345678", "david@company.comn"), "켄트백의 Tidy First?", 19800);

        System.out.println("주문개수: " + numberOfOrders);
    }

    private static void order(Customer customer, String productName, int price) {
        // TODO Auto-generated method stub
        numberOfOrders++;
        System.out.println(customer.toString());
        System.out.println("[고객: 이름:" + customer.getName() + ","
            + " 전화번호: " + customer.getPhoneNumber() + ","
            + " 이메일: " + customer.getEmail()
            + " ], 상품[ 이름: " + productName
            + ", 가격:" + price + "]");
    }

    private static void order(String customerName, String phoneNumber, String productName, int price) {
        numberOfOrders++;
        
        System.out.println("[고객: 이름:" + customerName + ","
            + " 전화번호: " + phoneNumber + " ], 상품[ 이름: " + productName
            + ", 가격:" + price + "]");
    }

    private static void order(String phoneNumber, String productName, int price) {
        order(null, phoneNumber, productName, price);
    }
}

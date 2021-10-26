using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Excel = Microsoft.Office.Interop.Excel;

namespace AppconExcel1
{
    public class Customer
    {
        public int customerId;
        public string fullName;

        public Customer(int customerId, string fullName)
        {
            this.customerId = customerId;
            this.fullName = fullName;
        }
    }

    public class Sale
    {
        public int saleId;
        public float saleAmount;
        public int customerId;
        public Sale(int saleId, float saleAmount, int customerId)
        {
            this.saleId = saleId;
            this.saleAmount = saleAmount;
            this.customerId = customerId;
        }
    }

    class Program
    {
        public static List<Customer> customers = new List<Customer>();
        public static List<Sale> sales = new List<Sale>();
        public static void generateSampleData()
        {
            // populate customers
            customers.Add(new Customer(1, "Alberto Cam"));
            customers.Add(new Customer(1, "Julia Lu"));
            customers.Add(new Customer(1, "Alfredo Chang"));
            customers.Add(new Customer(1, "Antonio Dong"));

            // populate sales
            sales.Add(new Sale(1, 100.0f, 1));
            sales.Add(new Sale(2, 150.0f, 3));
            sales.Add(new Sale(3, 250.0f, 2));
            sales.Add(new Sale(4, 15.00f, 4));
            sales.Add(new Sale(5, 17.50f, 1));
            sales.Add(new Sale(6, 110.0f, 1));
            sales.Add(new Sale(7, 99.0f, 2));
            sales.Add(new Sale(8, 189.0f, 3));
            sales.Add(new Sale(9, 210.0f, 4));
            sales.Add(new Sale(10, 75.0f, 3));
            sales.Add(new Sale(11, 11.0f, 2));
            sales.Add(new Sale(12, 80.0f, 2));
            sales.Add(new Sale(13, 89.99f, 3));
            sales.Add(new Sale(14, 120.88f, 1));
            sales.Add(new Sale(15, 76.60f, 2));
            sales.Add(new Sale(16, 24.50f, 4));
        }

        public static void Main(string[] args)
        {
            Excel.Application app = new Excel.Application();
            app.Visible = true;
            app.Workbooks.Add();
            app.Worksheets.Add();

            // populate Sales sheet
            Excel._Worksheet currentSheet = app.Sheets[1];
            currentSheet.Name = "Sales";
            currentSheet.Cells[1, "A"] = "Sale ID";
            currentSheet.Cells[1, "B"] = "Sale Amount";
            currentSheet.Cells[1, "C"] = "Customer ID";

            generateSampleData();

            for (int i = 0; i < sales.Count; i++)
            {
                currentSheet.Cells[2 + i, "A"] = sales[i].saleId;
                currentSheet.Cells[2 + i, "B"] = sales[i].saleAmount;
                currentSheet.Cells[2 + i, "C"] = sales[i].customerId;
            }

            currentSheet.Columns[1].AutoFit();
            currentSheet.Columns[2].AutoFit();
            currentSheet.Columns[3].AutoFit();

            // populate Customers sheet
            currentSheet = app.Sheets[2];
            currentSheet.Name = "Customers";
            currentSheet.Cells[1, "A"] = "Customer ID";
            currentSheet.Cells[1, "B"] = "Name";

            for (int i = 0; i < customers.Count; i++)
            {
                currentSheet.Cells[2 + i, "A"] = customers[i].customerId;
                currentSheet.Cells[2 + i, "B"] = customers[i].fullName;
            }

            currentSheet.Columns[1].AutoFit();
            currentSheet.Columns[2].AutoFit();

            // prevent console from closing
            Console.ReadLine();
        }
    }
}

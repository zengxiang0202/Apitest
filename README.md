allure报告报错。
![4b494385fa45a477260952b64606d0c](https://github.com/user-attachments/assets/731ee6e5-8569-49ee-8c3a-6b99afbc19a9)
![c100dbbbf4a11eb9d89c37cdf15b3dc](https://github.com/user-attachments/assets/db028f12-8e78-41ab-a03c-f06b34eb37a7)
解决点是在 os.system 命令中用双引号包裹 {report_path} 变量，确保整个路径被视为一个字符串。因为打印了report_path路径是D:\Program Files\Delivery_System-master\outFiles\report\temp。虽然看似合理但问题就出在Program Files这两个单词有空格了
命令行会将其解析为：
allure serve D:\Program
Files\Delivery_System-master\outFiles\report\temp
因此，命令会失败。修改之后，allure报告能成功打开。
![506acd423550d6f7dce8dc3a287f085](https://github.com/user-attachments/assets/93217d58-4d1f-488e-bab1-79cf5d4ff56a)

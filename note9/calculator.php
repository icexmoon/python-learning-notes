<?php
class Calculator
{
    private $a = 0;
    private $b = 0;

    /**
     * 构造函数
     * @param int $a
     * @param int $b
     */
    public function __construct($a, $b)
    {
        $this->a = $a;
        $this->b = $b;
    }

    /**
     * 求和
     * @return int
     */
    public function add()
    {
        $this->beforeRun(__FUNCTION__);
        return $this->a + $this->b;
    }

    /**
     * 执行数学计算前输出说明
     * @param string $operateName
     * @return void
     */
    private function beforeRun($operateName)
    {
        print("calculator will operate " . $operateName . "\n");
    }
}
$calculator = new Calculator(1, 2);
print($calculator->add());
<?php
require_once ".\\ContextInterface.php";
abstract class ContextCallable
{
    /**
     * @param ContextInterface $contextInterface
     */
    private $contextInterface;
    function __construct(ContextInterface $contextInterface)
    {
        $this->contextInterface = $contextInterface;
    }
    public function run()
    {
        $callBack = $this->contextInterface->enter();
        $this->action($callBack);
        $this->contextInterface->exit();
    }
    /**
     * 实现上下文中的业务逻辑
     * @param object $callBack 上下文协议接口返回的句柄
     */
    abstract protected function action($callBack);
}

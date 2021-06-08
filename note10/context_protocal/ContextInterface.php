<?php
interface ContextInterface{
    /**
     * 上下文准备环节
     * @return Object
     */
    public function enter();
    /**
     * 上下文清理环节
     */
    public function exit();
}
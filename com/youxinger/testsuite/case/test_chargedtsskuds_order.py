
from com.youxinger.testsuite.case.base_case import BaseCase
import logging
from com.youxinger.testsuite.service import market_service



class TestChargeGoods(BaseCase):
    """
   不同条码同SKU余额下单用例
    """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # 会员充值40000
        cls._customer.recharge(40000)

    def setUp(self):
        super().setUp()
        # 更新充值前的验证数据
        self._test_data.update_pre_verify_data()

    def tearDown(self):
        super().tearDown()

    def test_1_rechargesskudt_order(self):
        """
       不同条码同SKU余额下单
        :return:
        """
        logging.debug("test_1_rechargesskudt_order")
        params={
            'price': '19400.00', 'discount_money': '776.00', 'real_pay': '18624.00',
            'receive_name': self._customer.consignee, 'receive_phone': self._customer.phone,
            'receive_sheng': self._customer.province, 'receive_shi': self._customer.city,
            'receive_diqu': self._customer.area, 'receive_address': self._customer.address,
            'member_id': self._customer.member_number, 'member_name': self._customer.name,
            'member_phone': self._customer.phone,
            'plateform_id': self._customer.platform.platform_id,
            'special_employee_id': self._customer.employee.employee_id, 'discount_rate': '0.96',
            'goods_list[0][danjia]': '1000.00', 'goods_list[0][sku_num]': '3',
            'goods_list[0][sku_name]': '腰背夹',
            'goods_list[0][price]': '3000.00', 'goods_list[0][real_pay_price]': '2880.00',
            'goods_list[0][discount_price]': '120.00',
            'goods_list[0][sku_id]': '4878', 'goods_list[0][tiaoma]': 'M216C237C0458',
            'goods_list[0][kuanhao]': 'M216C237',
            'goods_list[0][sku_detail]': '深蓝色 58',
            'goods_list[0][img]': 'https://lchapp.oss-cn-beijing.aliyuncs.com/2019010579241063815.jpg',
            'goods_list[0][repo_out_num]': '3', 'goods_list[0][com_out_num]': '0',
            'goods_list[0][no_discount]': '0', 'goods_list[0][no_score]': '0',
            'goods_list[0][is_active]': '0', 'goods_list[0][type]': '2', 'goods_list[0][zh_num]': '1',
            'goods_list[0][zh_repo_out_num]': '1', 'goods_list[0][zh_com_out_num]': '0',
            'goods_list[0][zh_tiaoma]:': 'ZH02B215190T264284',
            'goods_list[0][zh_mark]': '1', 'goods_list[0][zh_no_discount]': '0',
            'goods_list[0][zh_no_score]': '0', 'goods_list[1][danjia]': '300.00',
            'goods_list[1][sku_num]': '1',
            'goods_list[1][sku_name]': '包臀内裤', 'goods_list[1][price]': '300.00',
            'goods_list[1][real_pay_price]': '288.00', 'goods_list[1][discount_price]': '12.00',
            'goods_list[1][sku_id]': '4701',
            'goods_list[1][tiaoma]': 'M116E248B0158', 'goods_list[1][kuanhao]': 'M116E248',
            'goods_list[1][sku_detail]': '黑色 58',
            'goods_list[1][img]': 'https://lchapp.oss-cn-beijing.aliyuncs.com/2019010568310459721.jpg',
            'goods_list[1][repo_out_num]': '1',
            'goods_list[1][com_out_num]': '0', 'goods_list[1][no_discount]': '0',
            'goods_list[1][no_score]': '0', 'goods_list[1][is_active]': '0', 'goods_list[1][type]': '2',
            'goods_list[1][zh_num]': '1', 'goods_list[1][zh_repo_out_num]': '1',
            'goods_list[1][zh_com_out_num]': '0', 'goods_list[1][zh_tiaoma]:': 'ZH02B215190T264284',
            'goods_list[1][zh_mark]': '1', 'goods_list[1][zh_no_discount]': '0',
            'goods_list[1][zh_no_score]': '0', 'goods_list[2][danjia]': '1000.00',
            'goods_list[2][sku_num]': '3',
            'goods_list[2][sku_name]': '腰背夹', 'goods_list[2][price]': '3000.00',
            'goods_list[2][real_pay_price]': '2880.00', 'goods_list[2][discount_price]': '120.00',
            'goods_list[2][sku_id]': '4878',
            'goods_list[2][tiaoma]': 'M216C237C0458', 'goods_list[2][kuanhao]': 'M216C237',
            'goods_list[2][sku_detail]': '深蓝色 58',
            'goods_list[2][img]': 'https://lchapp.oss-cn-beijing.aliyuncs.com/2019010579241063815.jpg',
            'goods_list[2][repo_out_num]': '0',
            'goods_list[2][com_out_num]': '3', 'goods_list[2][no_discount]': '0',
            'goods_list[2][no_score]': '0', 'goods_list[2][is_active]': '0', 'goods_list[2][type]': '2',
            'goods_list[2][zh_num]': '1', 'goods_list[2][zh_repo_out_num]': '0',
            'goods_list[2][zh_com_out_num]': '1', 'goods_list[2][zh_tiaoma]:': 'ZH02B215190T264284',
            'goods_list[2][zh_mark]': '2', 'goods_list[2][zh_no_discount]': '0',
            'goods_list[2][zh_no_score]': '0', 'goods_list[3][danjia]': '300.00',
            'goods_list[3][sku_num]': '1',
            'goods_list[3][sku_name]': '包臀内裤', 'goods_list[3][price]': '300.00',
            'goods_list[3][real_pay_price]': '288.00', 'goods_list[3][discount_price]': '12.00',
            'goods_list[3][sku_id]': '4701',
            'goods_list[3][tiaoma]': 'M116E248B0158', 'goods_list[3][kuanhao]': 'M116E248',
            'goods_list[3][sku_detail]': '黑色 58',
            'goods_list[3][img]': 'https://lchapp.oss-cn-beijing.aliyuncs.com/2019010568310459721.jpg',
            'goods_list[3][repo_out_num]': '0',
            'goods_list[3][com_out_num]': '1', 'goods_list[3][no_discount]': '0',
            'goods_list[3][no_score]': '0', 'goods_list[3][is_active]': '0', 'goods_list[3][type]': '2',
            'goods_list[3][zh_num]': '1', 'goods_list[3][zh_repo_out_num]': '0',
            'goods_list[3][zh_com_out_num]': '1', 'goods_list[3][zh_tiaoma]:': 'ZH02B215190T264284',
            'goods_list[3][zh_mark]': '2', 'goods_list[3][zh_no_discount]': '0',
            'goods_list[3][zh_no_score]': '0', 'goods_list[4][danjia]': '2000.00',
            'goods_list[4][sku_num]': '3',
            'goods_list[4][sku_name]': '腰背夹', 'goods_list[4][price]': '6000.00',
            'goods_list[4][real_pay_price]': '5760.00', 'goods_list[4][discount_price]': '240.00',
            'goods_list[4][sku_id]': '4878',
            'goods_list[4][tiaoma]': 'M216C237C0458', 'goods_list[4][kuanhao]': 'M216C237',
            'goods_list[4][sku_detail]': '深蓝色 58',
            'goods_list[4][img]': 'https://lchapp.oss-cn-beijing.aliyuncs.com/2019010579241063815.jpg',
            'goods_list[4][repo_out_num]': '0',
            'goods_list[4][com_out_num]': '3', 'goods_list[4][no_discount]': '0',
            'goods_list[4][no_score]': '0', 'goods_list[4][is_active]': '0', 'goods_list[4][type]': '2',
            'goods_list[4][zh_num]': '1', 'goods_list[4][zh_repo_out_num]': '1',
            'goods_list[4][zh_com_out_num]': '0', 'goods_list[4][zh_tiaoma]:': 'ZH02B215190T796242',
            'goods_list[4][zh_mark]': '3', 'goods_list[4][zh_no_discount]': '0',
            'goods_list[4][zh_no_score]': '0', 'goods_list[5][danjia]': '400.00',
            'goods_list[5][sku_num]': '1',
            'goods_list[5][sku_name]': '包臀内裤', 'goods_list[5][price]': '400.00',
            'goods_list[5][real_pay_price]': '384.00', 'goods_list[5][discount_price]': '16.00',
            'goods_list[5][sku_id]': '4701',
            'goods_list[5][tiaoma]': 'M116E248B0158', 'goods_list[5][kuanhao]': 'M116E248',
            'goods_list[5][sku_detail]': '黑色 58',
            'goods_list[5][img]': 'https://lchapp.oss-cn-beijing.aliyuncs.com/2019010568310459721.jpg',
            'goods_list[5][repo_out_num]': '0',
            'goods_list[5][com_out_num]': '1', 'goods_list[5][no_discount]': '0',
            'goods_list[5][no_score]': '0', 'goods_list[5][is_active]': '0', 'goods_list[5][type]': '2',
            'goods_list[5][zh_num]': '1', 'goods_list[5][zh_repo_out_num]': '0',
            'goods_list[5][zh_com_out_num]': '1', 'goods_list[5][zh_tiaoma]:': 'ZH02B215190T796242',
            'goods_list[5][zh_mark]': '3', 'goods_list[5][zh_no_discount]': '0',
            'goods_list[5][zh_no_score]': '0',
            'goods_list[6][danjia]': '2000.00',
            'goods_list[6][sku_num]': '3',
            'goods_list[6][sku_name]': '腰背夹', 'goods_list[6][price]': '6000.00',
            'goods_list[6][real_pay_price]': '5760.00', 'goods_list[6][discount_price]': '240.00',
            'goods_list[6][sku_id]': '4878',
            'goods_list[6][tiaoma]': 'M216C237C0458', 'goods_list[6][kuanhao]': 'M216C237',
            'goods_list[6][sku_detail]': '深蓝色 58',
            'goods_list[6][img]': 'https://lchapp.oss-cn-beijing.aliyuncs.com/2019010579241063815.jpg',
            'goods_list[6][repo_out_num]': '3',
            'goods_list[6][com_out_num]': '0', 'goods_list[6][no_discount]': '0',
            'goods_list[6][no_score]': '0', 'goods_list[6][is_active]': '0', 'goods_list[6][type]': '2',
            'goods_list[6][zh_num]': '1', 'goods_list[6][zh_repo_out_num]': '1',
            'goods_list[6][zh_com_out_num]': '0', 'goods_list[6][zh_tiaoma]:': 'ZH02B215190T796242',
            'goods_list[6][zh_mark]': '4', 'goods_list[6][zh_no_discount]': '0',
            'goods_list[6][zh_no_score]': '0',
            'goods_list[7][danjia]': '400.00',
            'goods_list[7][sku_num]': '1',
            'goods_list[7][sku_name]': '包臀内裤', 'goods_list[7][price]': '400.00',
            'goods_list[7][real_pay_price]': '384.00', 'goods_list[7][discount_price]': '16.00',
            'goods_list[7][sku_id]': '4701',
            'goods_list[7][tiaoma]': 'M116E248B0158', 'goods_list[7][kuanhao]': 'M116E248',
            'goods_list[7][sku_detail]': '黑色 58',
            'goods_list[7][img]': 'https://lchapp.oss-cn-beijing.aliyuncs.com/2019010568310459721.jpg',
            'goods_list[7][repo_out_num]': '1',
            'goods_list[7][com_out_num]': '0', 'goods_list[7][no_discount]': '0',
            'goods_list[7][no_score]': '0', 'goods_list[7][is_active]': '0', 'goods_list[7][type]': '2',
            'goods_list[7][zh_num]': '1', 'goods_list[7][zh_repo_out_num]': '1',
            'goods_list[7][zh_com_out_num]': '0', 'goods_list[7][zh_tiaoma]:': 'ZH02B215190T796242',
            'goods_list[7][zh_mark]': '4', 'goods_list[7][zh_no_discount]': '0',
            'goods_list[7][zh_no_score]': '0',

            'pay_type': 'recharge'

        }
        globals()['shopping_order_id']= market_service.recharge_order(params)
        # 更新充值后的验证数据
        self._test_data.update_post_verify_data()
        # 封装验证值
        self.expectedData(18624  # 会员消费额
                          , 0  # 会员积分
                          , 2  # 会员卡等级
                          , -18624  # 会员余额
                          , 0  # 总揽到店次数
                          , 0  # 总揽新增会员数
                          , 0  # 总揽订单数
                          , 0  # 总揽退单数
                          , 18624  # 总揽销售总额
                          , -6  # M216C237C0458总仓库存
                          , 0  # M216C237C0464总仓库存
                          , -2  # M116E248B0158总仓库存
                          , 0  # M116E248B0164总仓库存
                          , 0  # M316J232B01106总仓库存
                          , 0  # M316J232B0176总仓库存
                          , -2  # ZH02B215190T796242总仓库存
                          , 1.86  # 验证值
                          , -6  # M216C237C0458门店库存
                          , 0  # M216C237C0464门店库存
                          , -2  # M116E248B0158门店库存
                          , 0  # M116E248B0164门店库存
                          , 0  # M316J232B01106门店库存
                          , 0  # M316J232B0176门店库存
                          , 0 # ZH02B215190T796242门店库存
                          , 1  # 门店到店次数期待增加值
                          , 0  # 门店新增会员数期待增加值
                          , 1  # 门店订单数期待增加值
                          , 0  # 门店退单数期待增加值
                          , 18624  # 门店销售总额期待增加值
                          , 18624  # 门店平台销售总额期待增加值
                          )
        # 验证数据
        self._data_assertion()

    def test_2_rechargesskuds_return_part(self):
        """
       不同条码同SKU，部分退货
        :return:
        """
        logging.debug("test_2_rechargesskuds_return_part")
        if globals()['shopping_order_id'] is not None:
            returnOrderId = globals()['shopping_order_id'] + "_2"
            recharge_param={
                'main_order_id':globals()['shopping_order_id'],
                'return_price':'6144.00','reason':'15天无理由退货',
                'remarks':'第三方','afterSales_info[0][order_id]':returnOrderId ,
                'afterSales_info[0][danjia]':'6400.00',
                'afterSales_info[0][sku_name]':'孟伟组合商品',
                'afterSales_info[0][sku_detail]':'2件商品',
                'afterSales_info[0][tiaoma]':'ZH02B215190T796242',
                'afterSales_info[0][kuanhao]':'',
                'afterSales_info[0][sku_id]':'5955',
                'afterSales_info[0][img]':'https://lchapp.oss-cn-beijing.aliyuncs.com/2019080310765489321.jpg','afterSales_info[0][aftersale_num]':'1',
                'afterSales_info[0][aftersale_money]':'6144.00',
                'afterSales_info[0][goods_type]':'2'

            }
            market_service.return_order(recharge_param)
            # 更新充值后的验证数据
            self._test_data.update_post_verify_data()
            # 封装验证值
            self.expectedData(-6144  # 会员消费额
                              , 0  # 会员积分
                              , 2  # 会员卡等级
                              , 6144  # 会员余额
                              , 1  # 总揽到店次数
                              , 0  # 总揽新增会员数
                              , 1  # 总揽订单数
                              , 0  # 总揽退单数
                              , -6144  # 总揽销售总额
                              , 0  # M216C237C0458总仓库存
                              , 0  # M216C237C0464总仓库存
                              , 0  # M116E248B0158总仓库存
                              , 0  # M116E248B0164总仓库存
                              , 0  # M316J232B01106总仓库存
                              , 0  # M316J232B0176总仓库存
                              , 1  # ZH02B215190T796242总仓库存
                              , -0.61  # 验证值
                              , 3  # M216C237C0458门店库存
                              , 0  # M216C237C0464门店库存
                              , 1 # M116E248B0158门店库存
                              , 0  # M116E248B0164门店库存
                              , 0  # M316J232B01106门店库存
                              , 0  # M316J232B0176门店库存
                              , 0  # ZH02B215190T796242门店库存
                              , 0  # 门店到店次数期待增加值
                              , 0  # 门店新增会员数期待增加值
                              , 0  # 门店订单数期待增加值
                              , 1  # 门店退单数期待增加值
                              , -6144  # 门店销售总额期待增加值
                              , -6144  # 门店平台销售总额期待增加值
                              )
            # 验证数据
            self._data_assertion()





    def test_3_rechargesskuds_return_other(self):
                """
                同条码不同SKU，其余部分退货
                :return:
                """
                logging.debug("test_3_recharge_return_other")
                if globals()['shopping_order_id'] is not None:
                    returnOrderId = globals()['shopping_order_id'] + "_3"
                    returnOrderIdb=globals()['shopping_order_id'] + "_1"
                    returnOrderIda = globals()['shopping_order_id'] + "_0"
                    recharge_param = {
                        'main_order_id':globals()['shopping_order_id'],  'return_price':'12480.00',
                        'reason':'拍错/不想要',  'remarks':'',  'afterSales_info[0][order_id]':returnOrderId,
                        'afterSales_info[0][danjia]':'6400.00',
                        'afterSales_info[0][sku_name]':'孟伟组合商品',  'afterSales_info[0][sku_detail]':'2件商品',
                        'afterSales_info[0][tiaoma]':'ZH02B215190T796242',  'afterSales_info[0][kuanhao]':'',  'afterSales_info[0][sku_id]':'5955',
                        'afterSales_info[0][img]':'https://lchapp.oss-cn-beijing.aliyuncs.com/2019080310765489321.jpg',
                        'afterSales_info[0][aftersale_num]':'1','afterSales_info[0][aftersale_money]':'6144.00',
                        'afterSales_info[0][goods_type]':'2',
                        'afterSales_info[1][order_id]': returnOrderIdb, 'afterSales_info[1][danjia]': '3300.00',
                        'afterSales_info[1][sku_name]': '自动化测试勿删', 'afterSales_info[1][sku_detail]': '2件商品',
                        'afterSales_info[1][tiaoma]': 'ZH02B215190T264284', 'afterSales_info[1][kuanhao]': '',
                        'afterSales_info[1][sku_id]': '5973',
                        'afterSales_info[1][img]': 'https://lchapp.oss-cn-beijing.aliyuncs.com/2019080310765489321.jpg',
                        'afterSales_info[1][aftersale_num]': '1', 'afterSales_info[1][aftersale_money]': '3168.00',
                        'afterSales_info[1][goods_type]': '2','afterSales_info[2][order_id]':returnOrderIda,'afterSales_info[2][danjia]': '3300.00',
                        'afterSales_info[2][sku_name]': '自动化测试勿删', 'afterSales_info[2][sku_detail]': '2件商品',
                        'afterSales_info[2][tiaoma]': 'ZH02B215190T264284', 'afterSales_info[2][kuanhao]': '',
                        'afterSales_info[2][sku_id]': '5973',
                        'afterSales_info[2][img]': 'https://lchapp.oss-cn-beijing.aliyuncs.com/2019080310765489321.jpg',
                        'afterSales_info[2][aftersale_num]': '1', 'afterSales_info[2][aftersale_money]': '3168.00',
                        'afterSales_info[2][goods_type]': '2',

                    }
                    market_service.return_order(recharge_param)
                    # 更新充值后的验证数据
                    self._test_data.update_post_verify_data()
                    # 封装验证值
                    self.expectedData(-12480  # 会员消费额
                                      , 0  # 会员积分
                                      , 2  # 会员卡等级
                                      , 12480  # 会员余额
                                      , 0  # 总揽到店次数
                                      , 0  # 总揽新增会员数
                                      , 0  # 总揽订单数
                                      , 3  # 总揽退单数
                                      , -12480  # 总揽销售总额
                                      , 0  # M216C237C0458总仓库存
                                      , 0  # M216C237C0464总仓库存
                                      , 0  # M116E248B0158总仓库存
                                      , 0  # M116E248B0164总仓库存
                                      , 0  # M316J232B01106总仓库存
                                      , 0  # M316J232B0176总仓库存
                                      , 1  # ZH02B215190T796242总仓库存
                                      , -1.25  # 验证值
                                      , 9  # M216C237C0458门店库存
                                      , 0  # M216C237C0464门店库存
                                      , 3  # M116E248B0158门店库存
                                      , 0  # M116E248B0164门店库存
                                      , 0  # M316J232B01106门店库存
                                      , 0  # M316J232B0176门店库存
                                      , 0  # ZH02B215190T796242门店库存
                                      , 0  # 门店到店次数期待增加值
                                      , 0  # 门店新增会员数期待增加值
                                      , 0  # 门店订单数期待增加值
                                      , 3  # 门店退单数期待增加值
                                      , -12480  # 门店销售总额期待增加值
                                      , -12480  # 门店平台销售总额期待增加值
                                      )
                    # 验证数据
                    self._data_assertion()














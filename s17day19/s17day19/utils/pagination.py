class Page(object):
    def __init__(self, current_page, all_count,base_url, per_page=10, pager_page_count=11):
        '''
        分页的初始化
        :param current_page:当前页码 
        :param all_count: 数据库的总数据条数
        :param per_page: 每页显示的数据条数
         :param pager_page_count:页面上最多显示多少页码
        '''
        self.base_url=base_url
        self.current_page = current_page
        self.per_page = per_page
        self.all_count = all_count
        self.pager_page_count = pager_page_count
        pager_count, b = divmod(all_count, per_page)
        if b != 0:
            pager_count += 1
        # 总页码
        self.pager_count = pager_count

        #页码前后范围
        half_pager = int(pager_page_count / 2)
        self.half_pager = half_pager
    @property
    def start(self):
        '''
        :return:数据库获取值起始位置 
        '''
        start = (self.current_page - 1) * self.per_page
        return start
    @property
    def end(self):
        '''
        :return:数据库获取值结束位置 
        '''
        end = self.current_page * self.per_page
        return end

    def page_html(self):
        '''
        :return:生成html页码
        '''
        # 如果总页码不足
        if self.pager_count < self.pager_page_count:
            page_start = 1
            page_end = self.pager_count
        else:  # 数据已经超过11条 判断当前页的大小
            if self.current_page <= self.half_pager:
                page_start = 1
                page_end = 11
            else:
                # 如果当前页码+5大于总页码  结尾按总页码
                if self.current_page + 5 > self.pager_count:
                    page_end = self.pager_count
                    page_start = self.pager_count - self.per_page
                else:
                    page_start = self.current_page - self.half_pager
                    page_end = self.current_page + self.half_pager

        page_list = []
        if self.current_page == 1:
            prev = '<a href="#">上一页</a>'
        else:
            prev = '<a   href="%s?page=%s">上一页</a>' % (self.base_url,self.current_page - 1)
        page_list.append(prev)
        # for i in range(1,pager_count+1):
        for i in range(page_start, page_end + 1):
            if self.current_page == i:
                tp1 = '<a class="active" href="%s?page=%s">%s</a>' % (self.base_url,i, i,)
            else:
                tp1 = '<a href="%s?page=%s">%s</a>' % (self.base_url,i, i,)
            page_list.append(tp1)
        if self.current_page >= self.pager_count:
            nex = '<a href="#">下一页</a>'
        else:
            nex = '<a   href="%s?page=%s">下一页</a>' % (self.base_url,self.current_page + 1)
        page_list.append(nex)
        page_str = "".join(page_list)
        return page_str


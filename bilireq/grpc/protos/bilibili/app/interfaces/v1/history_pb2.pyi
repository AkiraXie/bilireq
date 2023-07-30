"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import bilireq.grpc.protos.bilibili.app.archive.middleware.v1.preload_pb2
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _DT:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _DTEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_DT.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    Unknown: _DT.ValueType  # 0
    """未知"""
    Phone: _DT.ValueType  # 1
    """手机端"""
    Pad: _DT.ValueType  # 2
    """ipad端"""
    PC: _DT.ValueType  # 3
    """web端"""
    TV: _DT.ValueType  # 4
    """TV端"""
    Car: _DT.ValueType  # 5
    """车机端"""
    Iot: _DT.ValueType  # 6
    """物联设备"""
    AndPad: _DT.ValueType  # 7
    """apad端"""

class DT(_DT, metaclass=_DTEnumTypeWrapper):
    """设备标识代码"""

Unknown: DT.ValueType  # 0
"""未知"""
Phone: DT.ValueType  # 1
"""手机端"""
Pad: DT.ValueType  # 2
"""ipad端"""
PC: DT.ValueType  # 3
"""web端"""
TV: DT.ValueType  # 4
"""TV端"""
Car: DT.ValueType  # 5
"""车机端"""
Iot: DT.ValueType  # 6
"""物联设备"""
AndPad: DT.ValueType  # 7
"""apad端"""
global___DT = DT

class _HistorySource:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _HistorySourceEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_HistorySource.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    history_VALUE: _HistorySource.ValueType  # 0
    """主站历史记录页"""
    shopping_VALUE: _HistorySource.ValueType  # 1
    """会员购浏览记录"""

class HistorySource(_HistorySource, metaclass=_HistorySourceEnumTypeWrapper):
    """搜索历史记录来源"""

history_VALUE: HistorySource.ValueType  # 0
"""主站历史记录页"""
shopping_VALUE: HistorySource.ValueType  # 1
"""会员购浏览记录"""
global___HistorySource = HistorySource

@typing_extensions.final
class CardArticle(google.protobuf.message.Message):
    """专栏卡片"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    COVERS_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    MID_FIELD_NUMBER: builtins.int
    DISPLAYATTENTION_FIELD_NUMBER: builtins.int
    BADGE_FIELD_NUMBER: builtins.int
    RELATION_FIELD_NUMBER: builtins.int
    @property
    def covers(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """封面url"""
    name: builtins.str
    """UP主昵称"""
    mid: builtins.int
    """UP主mid"""
    displayAttention: builtins.bool
    """是否展示关注按钮"""
    badge: builtins.str
    """角标"""
    @property
    def relation(self) -> global___Relation:
        """关系信息"""
    def __init__(
        self,
        *,
        covers: collections.abc.Iterable[builtins.str] | None = ...,
        name: builtins.str = ...,
        mid: builtins.int = ...,
        displayAttention: builtins.bool = ...,
        badge: builtins.str = ...,
        relation: global___Relation | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["relation", b"relation"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["badge", b"badge", "covers", b"covers", "displayAttention", b"displayAttention", "mid", b"mid", "name", b"name", "relation", b"relation"]) -> None: ...

global___CardArticle = CardArticle

@typing_extensions.final
class CardCheese(google.protobuf.message.Message):
    """课程卡片"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    COVER_FIELD_NUMBER: builtins.int
    PROGRESS_FIELD_NUMBER: builtins.int
    DURATION_FIELD_NUMBER: builtins.int
    SUBTITLE_FIELD_NUMBER: builtins.int
    STATE_FIELD_NUMBER: builtins.int
    cover: builtins.str
    """封面url"""
    progress: builtins.int
    """观看进度"""
    duration: builtins.int
    """总计时长"""
    subtitle: builtins.str
    """单集标题"""
    state: builtins.int
    """"""
    def __init__(
        self,
        *,
        cover: builtins.str = ...,
        progress: builtins.int = ...,
        duration: builtins.int = ...,
        subtitle: builtins.str = ...,
        state: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cover", b"cover", "duration", b"duration", "progress", b"progress", "state", b"state", "subtitle", b"subtitle"]) -> None: ...

global___CardCheese = CardCheese

@typing_extensions.final
class CardLive(google.protobuf.message.Message):
    """直播卡片"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    COVER_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    MID_FIELD_NUMBER: builtins.int
    TAG_FIELD_NUMBER: builtins.int
    STSTUS_FIELD_NUMBER: builtins.int
    DISPLAY_ATTENTION_FIELD_NUMBER: builtins.int
    RELATION_FIELD_NUMBER: builtins.int
    cover: builtins.str
    """封面url"""
    name: builtins.str
    """主播昵称"""
    mid: builtins.int
    """主播mid"""
    tag: builtins.str
    """直播分区名"""
    ststus: builtins.int
    """直播状态"""
    display_attention: builtins.bool
    """是否展示关注按钮"""
    @property
    def relation(self) -> global___Relation:
        """关系信息"""
    def __init__(
        self,
        *,
        cover: builtins.str = ...,
        name: builtins.str = ...,
        mid: builtins.int = ...,
        tag: builtins.str = ...,
        ststus: builtins.int = ...,
        display_attention: builtins.bool = ...,
        relation: global___Relation | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["relation", b"relation"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["cover", b"cover", "display_attention", b"display_attention", "mid", b"mid", "name", b"name", "relation", b"relation", "ststus", b"ststus", "tag", b"tag"]) -> None: ...

global___CardLive = CardLive

@typing_extensions.final
class CardOGV(google.protobuf.message.Message):
    """pgc稿件卡片"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    COVER_FIELD_NUMBER: builtins.int
    PROGRESS_FIELD_NUMBER: builtins.int
    DURATION_FIELD_NUMBER: builtins.int
    SUBTITLE_FIELD_NUMBER: builtins.int
    BADGE_FIELD_NUMBER: builtins.int
    STATE_FIELD_NUMBER: builtins.int
    cover: builtins.str
    """封面url"""
    progress: builtins.int
    """观看进度"""
    duration: builtins.int
    """总计时长"""
    subtitle: builtins.str
    """单集标题"""
    badge: builtins.str
    """"""
    state: builtins.int
    """"""
    def __init__(
        self,
        *,
        cover: builtins.str = ...,
        progress: builtins.int = ...,
        duration: builtins.int = ...,
        subtitle: builtins.str = ...,
        badge: builtins.str = ...,
        state: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["badge", b"badge", "cover", b"cover", "duration", b"duration", "progress", b"progress", "state", b"state", "subtitle", b"subtitle"]) -> None: ...

global___CardOGV = CardOGV

@typing_extensions.final
class CardUGC(google.protobuf.message.Message):
    """ugc稿件卡片"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    COVER_FIELD_NUMBER: builtins.int
    PROGRESS_FIELD_NUMBER: builtins.int
    DURATION_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    MID_FIELD_NUMBER: builtins.int
    DISPLAY_ATTENTION_FIELD_NUMBER: builtins.int
    CID_FIELD_NUMBER: builtins.int
    PAGE_FIELD_NUMBER: builtins.int
    SUBTITLE_FIELD_NUMBER: builtins.int
    RELATION_FIELD_NUMBER: builtins.int
    BVID_FIELD_NUMBER: builtins.int
    VIDEOS_FIELD_NUMBER: builtins.int
    SHORT_LINK_FIELD_NUMBER: builtins.int
    SHARE_SUBTITLE_FIELD_NUMBER: builtins.int
    VIEW_FIELD_NUMBER: builtins.int
    STATE_FIELD_NUMBER: builtins.int
    cover: builtins.str
    """封面url"""
    progress: builtins.int
    """观看进度"""
    duration: builtins.int
    """视频长度"""
    name: builtins.str
    """UP主昵称"""
    mid: builtins.int
    """UP主mid"""
    display_attention: builtins.bool
    """是否展示关注按钮"""
    cid: builtins.int
    """历史观看视频cid"""
    page: builtins.int
    """历史观看视频分P"""
    subtitle: builtins.str
    """历史观看视频分P的标题"""
    @property
    def relation(self) -> global___Relation:
        """关系信息"""
    bvid: builtins.str
    """稿件bvid"""
    videos: builtins.int
    """总分P数"""
    short_link: builtins.str
    """短链接"""
    share_subtitle: builtins.str
    """分享副标题"""
    view: builtins.int
    """播放数"""
    state: builtins.int
    """"""
    def __init__(
        self,
        *,
        cover: builtins.str = ...,
        progress: builtins.int = ...,
        duration: builtins.int = ...,
        name: builtins.str = ...,
        mid: builtins.int = ...,
        display_attention: builtins.bool = ...,
        cid: builtins.int = ...,
        page: builtins.int = ...,
        subtitle: builtins.str = ...,
        relation: global___Relation | None = ...,
        bvid: builtins.str = ...,
        videos: builtins.int = ...,
        short_link: builtins.str = ...,
        share_subtitle: builtins.str = ...,
        view: builtins.int = ...,
        state: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["relation", b"relation"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["bvid", b"bvid", "cid", b"cid", "cover", b"cover", "display_attention", b"display_attention", "duration", b"duration", "mid", b"mid", "name", b"name", "page", b"page", "progress", b"progress", "relation", b"relation", "share_subtitle", b"share_subtitle", "short_link", b"short_link", "state", b"state", "subtitle", b"subtitle", "videos", b"videos", "view", b"view"]) -> None: ...

global___CardUGC = CardUGC

@typing_extensions.final
class ClearReq(google.protobuf.message.Message):
    """清空历史记录-请求"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BUSINESS_FIELD_NUMBER: builtins.int
    business: builtins.str
    """业务类型
    archive:视频 live:直播 article:专栏 goods:商品 show:展演
    """
    def __init__(
        self,
        *,
        business: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["business", b"business"]) -> None: ...

global___ClearReq = ClearReq

@typing_extensions.final
class Cursor(google.protobuf.message.Message):
    """游标信息"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MAX_FIELD_NUMBER: builtins.int
    MAXTP_FIELD_NUMBER: builtins.int
    max: builtins.int
    """本页最大值游标值"""
    maxTp: builtins.int
    """本页最大值游标类型"""
    def __init__(
        self,
        *,
        max: builtins.int = ...,
        maxTp: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["max", b"max", "maxTp", b"maxTp"]) -> None: ...

global___Cursor = Cursor

@typing_extensions.final
class CursorItem(google.protobuf.message.Message):
    """历史记录卡片信息"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CARD_UGC_FIELD_NUMBER: builtins.int
    CARD_OGV_FIELD_NUMBER: builtins.int
    CARD_ARTICLE_FIELD_NUMBER: builtins.int
    CARD_LIVE_FIELD_NUMBER: builtins.int
    CARD_CHEESE_FIELD_NUMBER: builtins.int
    TITLE_FIELD_NUMBER: builtins.int
    URI_FIELD_NUMBER: builtins.int
    VIEWAT_FIELD_NUMBER: builtins.int
    KID_FIELD_NUMBER: builtins.int
    OID_FIELD_NUMBER: builtins.int
    BUSINESS_FIELD_NUMBER: builtins.int
    TP_FIELD_NUMBER: builtins.int
    DT_FIELD_NUMBER: builtins.int
    HAS_SHARE_FIELD_NUMBER: builtins.int
    @property
    def card_ugc(self) -> global___CardUGC:
        """ugc稿件"""
    @property
    def card_ogv(self) -> global___CardOGV:
        """pgc稿件"""
    @property
    def card_article(self) -> global___CardArticle:
        """专栏"""
    @property
    def card_live(self) -> global___CardLive:
        """直播"""
    @property
    def card_cheese(self) -> global___CardCheese:
        """课程"""
    title: builtins.str
    """标题"""
    uri: builtins.str
    """目标uri/url"""
    viewAt: builtins.int
    """观看时间"""
    kid: builtins.int
    """历史记录id"""
    oid: builtins.int
    """业务id"""
    business: builtins.str
    """业务类型
    archive:视频 live:直播 article:专栏 goods:商品 show:展演
    """
    tp: builtins.int
    """业务类型代码"""
    @property
    def dt(self) -> global___DeviceType:
        """设备标识"""
    has_share: builtins.bool
    """是否有分享按钮"""
    def __init__(
        self,
        *,
        card_ugc: global___CardUGC | None = ...,
        card_ogv: global___CardOGV | None = ...,
        card_article: global___CardArticle | None = ...,
        card_live: global___CardLive | None = ...,
        card_cheese: global___CardCheese | None = ...,
        title: builtins.str = ...,
        uri: builtins.str = ...,
        viewAt: builtins.int = ...,
        kid: builtins.int = ...,
        oid: builtins.int = ...,
        business: builtins.str = ...,
        tp: builtins.int = ...,
        dt: global___DeviceType | None = ...,
        has_share: builtins.bool = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["card_article", b"card_article", "card_cheese", b"card_cheese", "card_item", b"card_item", "card_live", b"card_live", "card_ogv", b"card_ogv", "card_ugc", b"card_ugc", "dt", b"dt"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["business", b"business", "card_article", b"card_article", "card_cheese", b"card_cheese", "card_item", b"card_item", "card_live", b"card_live", "card_ogv", b"card_ogv", "card_ugc", b"card_ugc", "dt", b"dt", "has_share", b"has_share", "kid", b"kid", "oid", b"oid", "title", b"title", "tp", b"tp", "uri", b"uri", "viewAt", b"viewAt"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["card_item", b"card_item"]) -> typing_extensions.Literal["card_ugc", "card_ogv", "card_article", "card_live", "card_cheese"] | None: ...

global___CursorItem = CursorItem

@typing_extensions.final
class CursorReply(google.protobuf.message.Message):
    """获取历史记录列表(旧版)-响应"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ITEMS_FIELD_NUMBER: builtins.int
    TAB_FIELD_NUMBER: builtins.int
    CURSOR_FIELD_NUMBER: builtins.int
    HASMORE_FIELD_NUMBER: builtins.int
    @property
    def items(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___CursorItem]:
        """卡片内容"""
    @property
    def tab(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___CursorTab]:
        """顶部tab"""
    @property
    def cursor(self) -> global___Cursor:
        """游标信息"""
    hasMore: builtins.bool
    """是否未拉取完"""
    def __init__(
        self,
        *,
        items: collections.abc.Iterable[global___CursorItem] | None = ...,
        tab: collections.abc.Iterable[global___CursorTab] | None = ...,
        cursor: global___Cursor | None = ...,
        hasMore: builtins.bool = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["cursor", b"cursor"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["cursor", b"cursor", "hasMore", b"hasMore", "items", b"items", "tab", b"tab"]) -> None: ...

global___CursorReply = CursorReply

@typing_extensions.final
class CursorReq(google.protobuf.message.Message):
    """获取历史记录列表(旧版)-请求"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CURSOR_FIELD_NUMBER: builtins.int
    BUSINESS_FIELD_NUMBER: builtins.int
    PLAYER_PRELOAD_FIELD_NUMBER: builtins.int
    PLAYER_ARGS_FIELD_NUMBER: builtins.int
    @property
    def cursor(self) -> global___Cursor:
        """游标信息"""
    business: builtins.str
    """业务类型
    all:全部 archive:视频 live:直播 article:专栏
    """
    @property
    def player_preload(self) -> global___PlayerPreloadParams:
        """秒开参数(旧版)"""
    @property
    def player_args(self) -> bilireq.grpc.protos.bilibili.app.archive.middleware.v1.preload_pb2.PlayerArgs:
        """秒开参数"""
    def __init__(
        self,
        *,
        cursor: global___Cursor | None = ...,
        business: builtins.str = ...,
        player_preload: global___PlayerPreloadParams | None = ...,
        player_args: bilireq.grpc.protos.bilibili.app.archive.middleware.v1.preload_pb2.PlayerArgs | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["cursor", b"cursor", "player_args", b"player_args", "player_preload", b"player_preload"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["business", b"business", "cursor", b"cursor", "player_args", b"player_args", "player_preload", b"player_preload"]) -> None: ...

global___CursorReq = CursorReq

@typing_extensions.final
class CursorTab(google.protobuf.message.Message):
    """业务分类表"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BUSINESS_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    ROUTER_FIELD_NUMBER: builtins.int
    FOCUS_FIELD_NUMBER: builtins.int
    business: builtins.str
    """业务类型"""
    name: builtins.str
    """名称"""
    router: builtins.str
    """路由uri"""
    focus: builtins.bool
    """tab定位"""
    def __init__(
        self,
        *,
        business: builtins.str = ...,
        name: builtins.str = ...,
        router: builtins.str = ...,
        focus: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["business", b"business", "focus", b"focus", "name", b"name", "router", b"router"]) -> None: ...

global___CursorTab = CursorTab

@typing_extensions.final
class CursorV2Reply(google.protobuf.message.Message):
    """获取历史记录列表-响应"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ITEMS_FIELD_NUMBER: builtins.int
    CURSOR_FIELD_NUMBER: builtins.int
    HASMORE_FIELD_NUMBER: builtins.int
    EMPTY_LINK_FIELD_NUMBER: builtins.int
    @property
    def items(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___CursorItem]:
        """卡片内容"""
    @property
    def cursor(self) -> global___Cursor:
        """游标信息"""
    hasMore: builtins.bool
    """是否未拉取完"""
    empty_link: builtins.str
    """"""
    def __init__(
        self,
        *,
        items: collections.abc.Iterable[global___CursorItem] | None = ...,
        cursor: global___Cursor | None = ...,
        hasMore: builtins.bool = ...,
        empty_link: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["cursor", b"cursor"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["cursor", b"cursor", "empty_link", b"empty_link", "hasMore", b"hasMore", "items", b"items"]) -> None: ...

global___CursorV2Reply = CursorV2Reply

@typing_extensions.final
class CursorV2Req(google.protobuf.message.Message):
    """获取历史记录列表-请求"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CURSOR_FIELD_NUMBER: builtins.int
    BUSINESS_FIELD_NUMBER: builtins.int
    PLAYER_PRELOAD_FIELD_NUMBER: builtins.int
    PLAYER_ARGS_FIELD_NUMBER: builtins.int
    IS_LOCAL_FIELD_NUMBER: builtins.int
    @property
    def cursor(self) -> global___Cursor:
        """游标信息"""
    business: builtins.str
    """业务类型
    archive:视频 live:直播 article:专栏 goods:商品 show:展演
    """
    @property
    def player_preload(self) -> global___PlayerPreloadParams:
        """秒开参数(旧版)"""
    @property
    def player_args(self) -> bilireq.grpc.protos.bilibili.app.archive.middleware.v1.preload_pb2.PlayerArgs:
        """秒开参数"""
    is_local: builtins.bool
    """是否选择本机的播放历史"""
    def __init__(
        self,
        *,
        cursor: global___Cursor | None = ...,
        business: builtins.str = ...,
        player_preload: global___PlayerPreloadParams | None = ...,
        player_args: bilireq.grpc.protos.bilibili.app.archive.middleware.v1.preload_pb2.PlayerArgs | None = ...,
        is_local: builtins.bool = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["cursor", b"cursor", "player_args", b"player_args", "player_preload", b"player_preload"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["business", b"business", "cursor", b"cursor", "is_local", b"is_local", "player_args", b"player_args", "player_preload", b"player_preload"]) -> None: ...

global___CursorV2Req = CursorV2Req

@typing_extensions.final
class DeleteReq(google.protobuf.message.Message):
    """删除历史记录-请求"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HIS_INFO_FIELD_NUMBER: builtins.int
    @property
    def his_info(self) -> global___HisInfo:
        """历史记录信息"""
    def __init__(
        self,
        *,
        his_info: global___HisInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["his_info", b"his_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["his_info", b"his_info"]) -> None: ...

global___DeleteReq = DeleteReq

@typing_extensions.final
class DeviceType(google.protobuf.message.Message):
    """设备类型"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TYPE_FIELD_NUMBER: builtins.int
    ICON_FIELD_NUMBER: builtins.int
    type: global___DT.ValueType
    """设备标识代码"""
    icon: builtins.str
    """图标url"""
    def __init__(
        self,
        *,
        type: global___DT.ValueType = ...,
        icon: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["icon", b"icon", "type", b"type"]) -> None: ...

global___DeviceType = DeviceType

@typing_extensions.final
class HisInfo(google.protobuf.message.Message):
    """历史记录信息"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BUSINESS_FIELD_NUMBER: builtins.int
    KID_FIELD_NUMBER: builtins.int
    business: builtins.str
    """业务类型
    archive:视频 live:直播 article:专栏 goods:商品 show:展演
    """
    kid: builtins.int
    """历史记录id"""
    def __init__(
        self,
        *,
        business: builtins.str = ...,
        kid: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["business", b"business", "kid", b"kid"]) -> None: ...

global___HisInfo = HisInfo

@typing_extensions.final
class HistoryTabReply(google.protobuf.message.Message):
    """获取历史记录tab-响应"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TAB_FIELD_NUMBER: builtins.int
    @property
    def tab(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___CursorTab]:
        """tab列表"""
    def __init__(
        self,
        *,
        tab: collections.abc.Iterable[global___CursorTab] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["tab", b"tab"]) -> None: ...

global___HistoryTabReply = HistoryTabReply

@typing_extensions.final
class HistoryTabReq(google.protobuf.message.Message):
    """获取历史记录tab-请求"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BUSINESS_FIELD_NUMBER: builtins.int
    SOURCE_FIELD_NUMBER: builtins.int
    KEYWORD_FIELD_NUMBER: builtins.int
    business: builtins.str
    """业务类型
    archive:视频 live:直播 article:专栏 goods:商品 show:展演
    """
    source: global___HistorySource.ValueType
    """查询请求来源"""
    keyword: builtins.str
    """搜索关键词"""
    def __init__(
        self,
        *,
        business: builtins.str = ...,
        source: global___HistorySource.ValueType = ...,
        keyword: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["business", b"business", "keyword", b"keyword", "source", b"source"]) -> None: ...

global___HistoryTabReq = HistoryTabReq

@typing_extensions.final
class LatestHistoryReply(google.protobuf.message.Message):
    """获取最新的历史记录-响应"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ITEMS_FIELD_NUMBER: builtins.int
    SCENE_FIELD_NUMBER: builtins.int
    RTIME_FIELD_NUMBER: builtins.int
    FLAG_FIELD_NUMBER: builtins.int
    @property
    def items(self) -> global___CursorItem:
        """卡片内容"""
    scene: builtins.str
    """场景"""
    rtime: builtins.int
    """弹窗停留时间"""
    flag: builtins.str
    """分组的标志(客户端埋点上报)"""
    def __init__(
        self,
        *,
        items: global___CursorItem | None = ...,
        scene: builtins.str = ...,
        rtime: builtins.int = ...,
        flag: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["items", b"items"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["flag", b"flag", "items", b"items", "rtime", b"rtime", "scene", b"scene"]) -> None: ...

global___LatestHistoryReply = LatestHistoryReply

@typing_extensions.final
class LatestHistoryReq(google.protobuf.message.Message):
    """获取最新的历史记录-请求"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BUSINESS_FIELD_NUMBER: builtins.int
    PLAYER_PRELOAD_FIELD_NUMBER: builtins.int
    business: builtins.str
    """业务类型
    archive:视频 live:直播 article:专栏 goods:商品 show:展演
    """
    @property
    def player_preload(self) -> global___PlayerPreloadParams:
        """秒开参数"""
    def __init__(
        self,
        *,
        business: builtins.str = ...,
        player_preload: global___PlayerPreloadParams | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["player_preload", b"player_preload"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["business", b"business", "player_preload", b"player_preload"]) -> None: ...

global___LatestHistoryReq = LatestHistoryReq

@typing_extensions.final
class NoReply(google.protobuf.message.Message):
    """空响应"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___NoReply = NoReply

@typing_extensions.final
class Page(google.protobuf.message.Message):
    """页面信息"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PN_FIELD_NUMBER: builtins.int
    TOTAL_FIELD_NUMBER: builtins.int
    pn: builtins.int
    """当前页码"""
    total: builtins.int
    """总计条目数"""
    def __init__(
        self,
        *,
        pn: builtins.int = ...,
        total: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["pn", b"pn", "total", b"total"]) -> None: ...

global___Page = Page

@typing_extensions.final
class PlayerPreloadParams(google.protobuf.message.Message):
    """秒开参数"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    QN_FIELD_NUMBER: builtins.int
    FNVER_FIELD_NUMBER: builtins.int
    FNVAL_FIELD_NUMBER: builtins.int
    FORCEHOST_FIELD_NUMBER: builtins.int
    FOURK_FIELD_NUMBER: builtins.int
    qn: builtins.int
    """清晰度"""
    fnver: builtins.int
    """流版本"""
    fnval: builtins.int
    """流类型"""
    forceHost: builtins.int
    """是否强制域名"""
    fourk: builtins.int
    """是否4K"""
    def __init__(
        self,
        *,
        qn: builtins.int = ...,
        fnver: builtins.int = ...,
        fnval: builtins.int = ...,
        forceHost: builtins.int = ...,
        fourk: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["fnval", b"fnval", "fnver", b"fnver", "forceHost", b"forceHost", "fourk", b"fourk", "qn", b"qn"]) -> None: ...

global___PlayerPreloadParams = PlayerPreloadParams

@typing_extensions.final
class Relation(google.protobuf.message.Message):
    """关系信息"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STATUS_FIELD_NUMBER: builtins.int
    IS_FOLLOW_FIELD_NUMBER: builtins.int
    IS_FOLLOWED_FIELD_NUMBER: builtins.int
    status: builtins.int
    """关系状态
    1:未关注 2:已关注 3:被关注 4:互关
    """
    is_follow: builtins.int
    """用户关注UP主"""
    is_followed: builtins.int
    """UP主关注用户"""
    def __init__(
        self,
        *,
        status: builtins.int = ...,
        is_follow: builtins.int = ...,
        is_followed: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["is_follow", b"is_follow", "is_followed", b"is_followed", "status", b"status"]) -> None: ...

global___Relation = Relation

@typing_extensions.final
class SearchReply(google.protobuf.message.Message):
    """搜索历史记录-响应"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ITEMS_FIELD_NUMBER: builtins.int
    HASMORE_FIELD_NUMBER: builtins.int
    PAGE_FIELD_NUMBER: builtins.int
    @property
    def items(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___CursorItem]:
        """卡片内容"""
    hasMore: builtins.bool
    """是否未拉取完"""
    @property
    def page(self) -> global___Page:
        """页面信息"""
    def __init__(
        self,
        *,
        items: collections.abc.Iterable[global___CursorItem] | None = ...,
        hasMore: builtins.bool = ...,
        page: global___Page | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["page", b"page"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["hasMore", b"hasMore", "items", b"items", "page", b"page"]) -> None: ...

global___SearchReply = SearchReply

@typing_extensions.final
class SearchReq(google.protobuf.message.Message):
    """搜索历史记录-请求"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    KEYWORD_FIELD_NUMBER: builtins.int
    PN_FIELD_NUMBER: builtins.int
    BUSINESS_FIELD_NUMBER: builtins.int
    keyword: builtins.str
    """关键词"""
    pn: builtins.int
    """页码"""
    business: builtins.str
    """业务类型
    archive:视频 live:直播 article:专栏 goods:商品 show:展演
    """
    def __init__(
        self,
        *,
        keyword: builtins.str = ...,
        pn: builtins.int = ...,
        business: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["business", b"business", "keyword", b"keyword", "pn", b"pn"]) -> None: ...

global___SearchReq = SearchReq

from streamlit_elements import mui
from .dashboard import Dashboard

class my_card(Dashboard.Item):

    DEFAULT_CONTENT = (
        """This impressive paella is a perfect party dish and a fun meal to cook 
        together with your guests. Add 1 cup of frozen peas along with the mussels, 
        if you like."""
    )

    def __call__(self,content):
        '''
        The function __call__() makes the class's object can be called directly as a method.
        i.e. if p = my_card() , p() is valid
        :param content: the content of this card
        :return: None
        '''
        with mui.Card(key=self._key,
                      sx={"display": "flex", "flexDirection": "column", "borderRadius": 3, "overflow": "hidden"}, elevation=1):
            mui.CardHeader(
                title="Shrimp and Chorizo Paella",
                subheader="September 14, 2016",
                avatar=mui.Avatar("R", sx={"bgcolor": "red"}),
                action=mui.IconButton(mui.icon.MoreVert),
                className=self._draggable_class,
            )
            with mui.CardContent(sx={"flex": 1}):
                mui.Typography(content)
            # with mui.CardActions(disableSpacing=True):
            #     mui.IconButton(mui.icon.Favorite)
            #     mui.IconButton(mui.icon.Share)

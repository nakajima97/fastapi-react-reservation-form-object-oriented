import {
  AppBar,
  Toolbar,
  Box,
  Typography,
  Drawer,
  List,
  ListItem,
  Button,
} from "@mui/material";

const ReservationIndexPage = () => {
  const sideBarBarWidth = "240px";

  return (
    <Box sx={{ display: "flex" }}>
      <AppBar position="fixed">
        <Toolbar>
          <Typography>予約一覧</Typography>
        </Toolbar>
      </AppBar>
      <Box sx={{ flexShrink: 0, width: sideBarBarWidth, borderRight: "1px" }}>
        {/* 高さ確保用 */}
        <Toolbar />
        <Box sx={{ overflow: "auto" }}>
          <List>
            <ListItem>
              <Button>予約一覧</Button>
            </ListItem>
            <ListItem>
              <Button>営業日設定</Button>
            </ListItem>
          </List>
        </Box>
      </Box>
      <Box sx={{ flexShrink: 1, p: 3 }}>
        {/* 高さ確保用 */}
        <Toolbar />
        メイン
      </Box>
    </Box>
  );
};

export default ReservationIndexPage;

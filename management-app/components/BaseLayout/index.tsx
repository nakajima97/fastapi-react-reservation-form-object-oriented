"use client";

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
import { FunctionComponent } from "react";

type Props = {
  children: React.ReactElement;
};

const BaseLayout: FunctionComponent<Props> = ({ children }) => {
  const drawerWidth = "140px";

  return (
    <Box sx={{ display: "flex" }}>
      <AppBar
        position="fixed"
        sx={{ zIndex: (theme) => theme.zIndex.drawer + 1 }}
      >
        <Toolbar>
          <Typography>予約一覧</Typography>
        </Toolbar>
      </AppBar>
      <Drawer
        variant="permanent"
        sx={{
          width: drawerWidth,
          flexShrink: 0,
          [`& .MuiDrawer-paper`]: {
            width: drawerWidth,
            boxSizing: "border-box",
          },
        }}
      >
        {/* 高さ確保用 */}
        <Toolbar />
        <Box sx={{ overflow: "auto", width: "100%" }}>
          <List>
            <ListItem>
              <Button>予約一覧</Button>
            </ListItem>
            <ListItem>
              <Button>営業日設定</Button>
            </ListItem>
          </List>
        </Box>
      </Drawer>
      <Box sx={{ flexShrink: 1, p: 3 }}>
        {/* 高さ確保用 */}
        <Toolbar />
        {children}
      </Box>
    </Box>
  );
};

export default BaseLayout;

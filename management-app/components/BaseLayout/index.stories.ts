import type { Meta, StoryObj } from "@storybook/react";
import BaseLayout from "./index";

const meta: Meta = {
  title: "BaseLayout",
  component: BaseLayout,
  parameters: {
    nextjs: {
      appDirectory: true,
    },
  },
};
export default meta;

export const Primary: StoryObj<typeof meta> = {
  args: {
    title: "BaseLayout",
  },
};

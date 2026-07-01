import type { IconType } from "react-icons";

export interface NavItem {
  label: string;
  icon: IconType;
}

export interface User {
  id: number;
  name: string;
  email: string;
}

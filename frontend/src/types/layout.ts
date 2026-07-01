import type { IconType } from "react-icons";

export type BackendUserRole = "SOLIDARIO" | "PROFESIONAL" | "ESPECIALIZADO";
export type CaregiverRole = BackendUserRole;

export interface CaregiverRestrictions {
  species: string[];
  sizes: string[];
  medications: boolean;
}

export interface CaregiverProfile {
  role: CaregiverRole;
  restrictions: CaregiverRestrictions;
  receiveAlerts: boolean;
  ratingAverage: number;
}

export interface NavItem {
  label: string;
  icon: IconType;
}

export interface User {
  id: number;
  name: string;
  email: string;
  role: string;
}

export interface Notification {
  alert_id: number;
  text: string;
}


import React from 'react';
import { Button } from '@/components/ui/button';
import { LogOut, HelpCircle, ChevronDown } from 'lucide-react';
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from '@/components/ui/dropdown-menu';

const Header = () => {
  const handleLogout = () => {
    console.log('Logout clicked');
    // Add logout logic here
  };

  const handleHelp = () => {
    console.log('Help clicked');
    // Add help logic here
  };

  return (
    <div className="bg-white border-b border-gray-200 p-6">
      <div className="flex items-center justify-between">
        <div className="flex items-center space-x-6">
          <select className="border border-gray-300 rounded px-4 py-3 text-base">
            <option>Mounting 2</option>
            <option>Mounting 1</option>
            <option>Mounting 3</option>
          </select>
          <select className="border border-gray-300 rounded px-4 py-3 text-base">
            <option>Last 7 days</option>
            <option>Last 24 hours</option>
            <option>Last 30 days</option>
          </select>
          <Button className="bg-blue-600 hover:bg-blue-700 text-white px-8 py-3 text-base">
            REFRESH
          </Button>
        </div>
        <div className="flex items-center space-x-6">
          <Button
            variant="ghost"
            size="sm"
            onClick={handleHelp}
            className="text-gray-600 hover:text-gray-900"
          >
            <HelpCircle size={20} />
            <span className="ml-2">Help</span>
          </Button>
          
          <DropdownMenu>
            <DropdownMenuTrigger asChild>
              <Button variant="ghost" className="flex items-center space-x-3">
                <span className="text-base text-gray-600">Admin User</span>
                <div className="w-10 h-10 bg-gray-400 rounded-full"></div>
                <ChevronDown size={16} />
              </Button>
            </DropdownMenuTrigger>
            <DropdownMenuContent align="end" className="w-48 bg-white shadow-lg border">
              <DropdownMenuItem onClick={handleLogout} className="cursor-pointer">
                <LogOut size={16} />
                <span className="ml-2">Logout</span>
              </DropdownMenuItem>
            </DropdownMenuContent>
          </DropdownMenu>
        </div>
      </div>
    </div>
  );
};

export default Header;

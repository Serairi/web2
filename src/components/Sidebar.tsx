
import React, { useState } from 'react';
import { ChevronDown, ChevronRight } from 'lucide-react';

interface MenuItem {
  title: string;
  items?: string[];
  isExpanded?: boolean;
}

const Sidebar = () => {
  const [menuItems, setMenuItems] = useState<MenuItem[]>([
    {
      title: 'Master Data',
      items: ['Part Type', 'Part Master', 'Part Group'],
      isExpanded: true
    },
    {
      title: 'Work Plan Data',
      items: ['Work Plan', 'Work Step Catalog'],
      isExpanded: false
    },
    {
      title: 'Production Means',
      items: [],
      isExpanded: false
    },
    {
      title: 'Orders',
      items: ['Order Management'],
      isExpanded: false
    },
    {
      title: 'Maintenance',
      items: ['Failure Definition', 'Machine condition'],
      isExpanded: false
    },
    {
      title: 'BOM',
      items: [],
      isExpanded: false
    },
    {
      title: 'Tracking',
      items: [],
      isExpanded: false
    },
    {
      title: 'BI',
      items: [],
      isExpanded: false
    },
    {
      title: 'IIOT',
      items: [],
      isExpanded: false
    },
    {
      title: 'KPI',
      items: [],
      isExpanded: false
    },
    {
      title: 'Low-Code',
      items: [],
      isExpanded: false
    }
  ]);

  const toggleMenu = (index: number) => {
    setMenuItems(prev => prev.map((item, i) => 
      i === index ? { ...item, isExpanded: !item.isExpanded } : item
    ));
  };

  return (
    <div className="w-64 bg-gray-900 text-white min-h-screen p-4">
      <div className="space-y-2">
        {menuItems.map((item, index) => (
          <div key={item.title}>
            <div 
              className="flex items-center justify-between p-2 hover:bg-gray-800 cursor-pointer rounded"
              onClick={() => toggleMenu(index)}
            >
              <span className="text-sm">{item.title}</span>
              {item.items && item.items.length > 0 && (
                item.isExpanded ? <ChevronDown size={16} /> : <ChevronRight size={16} />
              )}
            </div>
            {item.isExpanded && item.items && (
              <div className="ml-4 space-y-1">
                {item.items.map((subItem) => (
                  <div 
                    key={subItem} 
                    className="p-2 text-sm text-gray-300 hover:bg-gray-800 cursor-pointer rounded"
                  >
                    {subItem}
                  </div>
                ))}
              </div>
            )}
          </div>
        ))}
      </div>
    </div>
  );
};

export default Sidebar;
